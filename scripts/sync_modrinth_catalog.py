#!/usr/bin/env python3
"""Refresh a small plugin discovery snapshot using the official Modrinth API."""
from __future__ import annotations

import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "plugin-catalog.json"
API = "https://api.modrinth.com/v2"
USER_AGENT = os.environ.get("MODRINTH_USER_AGENT", "CraftLens/0.1 (https://github.com/wuyixiao123/craftlens)")
LIMIT = 20


def get_json(url: str):
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    for attempt in range(3):
        try:
            with urlopen(request, timeout=30) as response:
                return json.load(response)
        except HTTPError as exc:
            if exc.code == 429 and attempt < 2:
                time.sleep(3 * (attempt + 1))
                continue
            raise
        except (TimeoutError, URLError):
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"Request failed: {url}")


def search_projects(sort: str) -> list[dict]:
    params = {
        "limit": str(LIMIT),
        "index": sort,
        "facets": json.dumps([["project_type:plugin"]], separators=(",", ":")),
    }
    data = get_json(f"{API}/search?{urlencode(params)}")
    return data.get("hits", [])


def main() -> int:
    try:
        merged: dict[str, dict] = {}
        for sort in ("downloads", "updated"):
            for item in search_projects(sort):
                project_id = item.get("project_id")
                if not project_id:
                    continue
                if project_id not in merged:
                    merged[project_id] = item
                merged[project_id].setdefault("catalog_reasons", [])
                if sort == "downloads":
                    merged[project_id]["catalog_reasons"].append("popular")
                else:
                    merged[project_id]["catalog_reasons"].append("recently-updated")

        projects = []
        for item in merged.values():
            projects.append({
                "id": item.get("project_id", ""),
                "slug": item.get("slug", ""),
                "title": item.get("title", ""),
                "description": item.get("description", ""),
                "downloads": int(item.get("downloads") or 0),
                "followers": int(item.get("follows") or 0),
                "updated": item.get("date_modified", ""),
                "updated_label": (item.get("date_modified") or "")[:10],
                "game_versions": item.get("versions", []),
                "loaders": item.get("loaders", []),
                "categories": item.get("categories", []),
                "catalog_reasons": sorted(set(item.get("catalog_reasons", []))),
                "url": "https://modrinth.com/plugin/" + item.get("slug", ""),
                "source": "Modrinth official API",
            })
        projects.sort(key=lambda p: (p["downloads"], p["title"].lower()), reverse=True)
        payload = {
            "schema_version": 1,
            "source": "Modrinth official API",
            "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "count": len(projects),
            "projects": projects,
            "disclaimer": "Discovery snapshot only. Metadata can be incomplete or change upstream. Check the original project and version page before upgrading.",
        }
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"Updated {OUTPUT.relative_to(ROOT)} with {len(projects)} projects.")
        return 0
    except Exception as exc:  # Keep CI failure explicit; never silently overwrite with empty data.
        print(f"ERROR: Modrinth catalog sync failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
