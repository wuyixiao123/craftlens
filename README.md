# CraftLens

**Minecraft compatibility, without the guesswork.**

CraftLens is an open-source, source-linked compatibility explorer for Minecraft Java Edition. It helps players and server administrators compare Minecraft versions, Java requirements, server software, and mod-loader ecosystems before upgrading.

> **Data integrity first:** CraftLens distinguishes verified facts, community-maintained notes, and unknown compatibility. It does not claim that every mod or plugin has been tested. Always check the upstream project's release notes before upgrading a production server.

## What works today

- Search and filter a small, curated Minecraft Java version reference.
- Compare Java runtime guidance and common server / mod-loader considerations.
- See evidence links and the last review date for each record.
- Run a local data validation check.
- Automatically validate the dataset daily with GitHub Actions.

## Try it

Open the hosted site (after enabling GitHub Pages):  
**https://wuyixiao123.github.io/craftlens/**

Or run locally: download the repository and open `index.html` in a browser. No build step, account, backend, or API key is required.

## Data policy

- A missing record means **unknown**, not compatible.
- Compatibility can differ between a project's versions, loader, and dependencies.
- Every factual record should include an evidence URL and review date.
- Automation validates structure; it must not invent compatibility results.
- Do not use this project as the sole basis for a production upgrade. Back up first.

## Contribute

Issues and pull requests are welcome. Please include the exact Minecraft version, Java runtime, server software or loader, affected project version, reproduction steps, and upstream evidence where possible.

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and [LICENSE](LICENSE).

## Roadmap

- [x] Searchable, responsive compatibility reference
- [x] Source links and explicit confidence labels
- [x] Automated dataset validation
- [ ] Expand curated version and loader records with upstream evidence
- [ ] Add a guided server-upgrade checklist
- [ ] Add a safe, privacy-respecting crash-log helper

## License

MIT. See [LICENSE](LICENSE).
