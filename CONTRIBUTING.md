# Contributing to CraftLens

Thanks for helping make compatibility information clearer and more reliable.

## Report a compatibility issue

Include as many of these as possible:
- Minecraft Java Edition version
- Java runtime and version
- Server software or mod loader, including its exact build
- Mod/plugin name and exact version
- Expected behavior and actual behavior
- Reproduction steps and relevant upstream links

Never upload private tokens, server credentials, personal information, or a complete log containing secrets.

## Add or update a dataset record

1. Edit `data/compatibility.json`.
2. Give each record a stable, unique `id`.
3. Include at least one direct HTTPS evidence link and a human-readable label.
4. Set `reviewed` to the date you actually checked the evidence.
5. Use `documented` only for a narrow claim supported by evidence. Use `verify-upstream` when users must confirm the exact build or dependencies.
6. Never infer mod/plugin compatibility solely from a Minecraft version or loader.
7. Run `python scripts/validate_data.py` and inspect the rendered page locally.

## Local preview

Run `python -m http.server 8000` from the repository root and open http://localhost:8000.

Pull requests should explain what changed and include sources for factual compatibility claims.
