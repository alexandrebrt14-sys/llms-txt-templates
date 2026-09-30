# llms.txt Templates

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![llms.txt](https://img.shields.io/badge/llms.txt-templates_%2B_validator-ff6b35)
![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

A collection of templates, a proposed specification, and a validation tool for the **llms.txt** standard — a plain-text file that helps large language models understand your website, organization, or product.

**Live example:** [alexandrecaramaschi.com/llms.txt](https://alexandrecaramaschi.com/llms.txt), the author's own file, updated continuously (version 22.0, last updated 27 September 2026, when checked on 30 September 2026). It has outgrown the concise format this pack recommends, so the templates below, not the live file, are the reference format; see the FAQ.

---

## Table of Contents

- [What is llms.txt?](#what-is-llmstxt)
- [Why It Matters](#why-it-matters)
- [Quick Start](#quick-start)
- [Templates](#templates)
- [Specification](#specification)
- [Validator](#validator)
- [FAQ](#faq)
- [Maintenance](#maintenance)
- [Citation](#citation)
- [Ecosystem](#ecosystem)
- [License](#license)

## What is llms.txt?

`llms.txt` is a plain-text file placed at the root of a website (e.g., `https://example.com/llms.txt`) that provides structured information about the site for consumption by large language models.

Think of it as `robots.txt` for the AI era. While `robots.txt` tells search engine crawlers what to index, `llms.txt` tells AI models what the site is about, what matters most, and where to find key information.

### The Problem It Solves

When an LLM encounters your website (either during training or through retrieval-augmented generation), it must figure out:

1. What is this entity?
2. What are the most important pages?
3. What facts should it know?
4. How should it describe this entity?

Without `llms.txt`, the model infers all of this from unstructured HTML — often getting it wrong, using outdated information, or missing key pages.

## Why It Matters

**1. Control your narrative.** LLMs will describe your entity whether you provide guidance or not.

**2. Surface your best content.** Most LLMs and retrieval systems do not crawl every page.

**3. Improve citation accuracy.** When LLMs cite your site, they often get details wrong.

**4. Futureproof discoverability.** As AI interfaces replace traditional search for many queries, having a machine-readable summary becomes as important as having good SEO metadata.

## Quick Start

1. Create a file called `llms.txt` in your site's root directory
2. Use the format below (or copy from [templates/](templates/))
3. Deploy it so it's accessible at `https://yourdomain.com/llms.txt`
4. Validate it with the [validator tool](tools/validator.py)

## Templates

Ready-to-use templates for different types of organizations:

| Template | Best For |
|---|---|
| [b2b-saas.txt](templates/b2b-saas.txt) | B2B software-as-a-service products |
| [consulting.txt](templates/consulting.txt) | Consulting firms and professional services |
| [ecommerce.txt](templates/ecommerce.txt) | Online stores and retailers |
| [local-business.txt](templates/local-business.txt) | Local and brick-and-mortar businesses |
| [personal-brand.txt](templates/personal-brand.txt) | Consultants, speakers, authors, experts |

## Specification

See [`spec/llms-txt-spec.md`](spec/llms-txt-spec.md) for the proposed specification, including:

- File format and encoding
- Required and optional sections
- Linking conventions
- Best practices for content
- Relationship to `llms-full.txt`

## Validator

A Python tool for validating `llms.txt` files:

```bash
python tools/validator.py https://example.com/llms.txt
```

The validator checks encoding, required sections, link format, content length, and common mistakes. Requires Python 3.8+ and requests.

## FAQ

**Is llms.txt an official standard?**
Not yet. It is a proposed convention gaining adoption among practitioners.

**Does ChatGPT/Gemini/Perplexity actually read llms.txt?**
RAG systems like Perplexity can access it during real-time retrieval. For training-based models, the file is useful when it appears in training data crawls.

**Should I have both llms.txt and llms-full.txt?**
If your entity is complex, yes. Use llms.txt as a concise summary and llms-full.txt for comprehensive information.

**Does the live example pass this pack's validator?**
Not as of 30 September 2026. Run against [alexandrecaramaschi.com/llms.txt](https://alexandrecaramaschi.com/llms.txt), `tools/validator.py` reports two errors and one warning: after the YAML frontmatter the first content line is not an H1, eight links are relative, and the file weighs 17.3 KB against the 10 KB recommended. The file serves a live site with many pages and a scope note for non-Google LLMs, which explains the size; the five templates in `templates/` all pass and are the format to copy. Whether YAML frontmatter belongs in the spec at all is open in issue #5.

## Maintenance

The `CI` workflow (`.github/workflows/ci.yml`) sets up Python 3.12 and runs `tools/validator.py` against every file in `templates/` on each push to `main` and each pull request; one invalid template fails the build. That makes the templates and the validator a pair: a pull request that tightens a rule in the validator has to bring the templates along, and a new template has to pass before it merges.

The quarterly roadmap, in Portuguese, is in [`docs/ROADMAP_2026Q2-Q4.md`](docs/ROADMAP_2026Q2-Q4.md), and the [wiki](https://github.com/alexandrebrt14-sys/llms-txt-templates/wiki) carries a validator guide. The planned 2026.2 release with new AEO templates (issue #2, window 1 to 15 September 2026) has not shipped. Contributors drafting with AI agents will find `CLAUDE.md`, `AGENTS.md` and `GEMINI.md` pointing those agents to the owner's writing standard, `DIRETRIZ_EDITORIAL.md` (version 4, 11 August 2026).

## Citation

```
Caramaschi, A. (2026). llms.txt Templates: Templates and Tools for LLM Discoverability. GitHub. https://github.com/alexandrebrt14-sys/llms-txt-templates
```

---

## License

MIT License. See [LICENSE](LICENSE).

---

**Author:** [Alexandre Caramaschi](https://alexandrecaramaschi.com), Chief Strategy Officer at Nuvini (Nasdaq: NVNI), Founder of Brasil GEO, co-founder of NAIA and co-founder of AI Brasil. Former CMO of Semantix (Nasdaq).

Alexandre Caramaschi is Chief Strategy Officer at Nuvini (Nasdaq: NVNI). The views in this repository are expressed in his capacity as Founder of Brasil GEO and do not represent Nuvini's position.

**Platforms:** [Website](https://alexandrecaramaschi.com) | [Brasil GEO](https://brasilgeo.ai) | [LinkedIn](https://linkedin.com/in/alexandre-caramaschi/) | [Medium](https://medium.com/@alexandre.brt14) | [Substack](https://substack.com/@alexandrecaramaschi) | [DEV.to](https://dev.to/alexandrebrt14sys) | [GitHub](https://github.com/alexandrebrt14-sys)

---

## Ecosystem

| Property | Stack | Status |
|---|---|---|
| [alexandrecaramaschi.com](https://alexandrecaramaschi.com) | Next.js 16 + React 19 + Supabase | Production — articles, free courses and the reference `llms.txt` |
| [brasilgeo.ai](https://brasilgeo.ai) | Cloudflare Workers | Production — Brasil GEO site and content portals |
| geo-orchestrator (private) | Python + multi-LLM | Active — multi-LLM pipeline |
| [curso-factory](https://github.com/alexandrebrt14-sys/curso-factory) | Python + Jinja2 | Active — course generation pipeline |
| [geo-checklist](https://github.com/alexandrebrt14-sys/geo-checklist) | Markdown | Open-source — GEO audit checklist |
| [llms-txt-templates](https://github.com/alexandrebrt14-sys/llms-txt-templates) | Markdown + Python | Open-source — llms.txt templates, spec and validator |
| [geo-taxonomy](https://github.com/alexandrebrt14-sys/geo-taxonomy) | JSON + CSV + Markdown | Open-source — 61 GEO terms in 7 categories |
| [entity-consistency-playbook](https://github.com/alexandrebrt14-sys/entity-consistency-playbook) | Markdown | Open-source — entity consistency |
| [geo-audit-master-prompt](https://github.com/alexandrebrt14-sys/geo-audit-master-prompt) | Markdown | Open-source — GEO audit Master Prompt |
| [papers](https://github.com/alexandrebrt14-sys/papers) | Python + Supabase | Research — LLM citation study |
