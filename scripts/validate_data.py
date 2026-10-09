#!/usr/bin/env python3
"""Validate CraftLens's public compatibility dataset without third-party packages."""
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "compatibility.json"

def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)

def main() -> None:
    try:
        payload = json.loads(DATA.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"cannot read valid JSON from {DATA}: {exc}")
    if payload.get("schema_version") != 1:
        fail("schema_version must be 1")
    try:
        date.fromisoformat(payload["last_reviewed"])
    except (KeyError, TypeError, ValueError):
        fail("last_reviewed must be an ISO date")
    records = payload.get("records")
    if not isinstance(records, list) or not records:
        fail("records must be a non-empty array")
    ids = set()
    for i, record in enumerate(records):
        prefix = f"records[{i}]"
        for key in ("id", "kind", "name", "version", "java", "status", "confidence", "summary", "reviewed", "evidence"):
            if not record.get(key):
                fail(f"{prefix}.{key} is required")
        if record["id"] in ids:
            fail(f"duplicate record id: {record['id']}")
        ids.add(record["id"])
        if record["status"] not in {"documented", "verify-upstream"}:
            fail(f"{prefix}.status is not an allowed value")
        if record["confidence"] not in {"high", "medium", "low"}:
            fail(f"{prefix}.confidence is not an allowed value")
        try:
            date.fromisoformat(record["reviewed"])
        except (TypeError, ValueError):
            fail(f"{prefix}.reviewed must be an ISO date")
        if not isinstance(record["evidence"], list) or not record["evidence"]:
            fail(f"{prefix}.evidence must contain at least one source")
        for j, evidence in enumerate(record["evidence"]):
            url = evidence.get("url", "")
            parsed = urlparse(url)
            if not evidence.get("label") or parsed.scheme != "https" or not parsed.netloc:
                fail(f"{prefix}.evidence[{j}] must have a label and HTTPS URL")
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    if 'fetch("./data/compatibility.json")' not in html:
        fail("index.html does not load the expected dataset")
    print(f"OK: {len(records)} records, unique IDs, dates, evidence URLs, and app data path validated.")

if __name__ == "__main__":
    main()
