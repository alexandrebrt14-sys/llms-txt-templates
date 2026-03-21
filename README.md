# llms.txt Examples

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A collection of templates, a proposed specification, and a validation tool for the **llms.txt** standard — a plain-text file that helps large language models understand your website, organization, or product.

---

## Table of Contents

- [What is llms.txt?](#what-is-llmstxt)
- [Why It Matters](#why-it-matters)
- [Quick Start](#quick-start)
- [Templates](#templates)
- [Specification](#specification)
- [Validator](#validator)
- [FAQ](#faq)
- [Citation](#citation)
- [License](#license)

## What is llms.txt?

\`llms.txt\` is a plain-text file placed at the root of a website (e.g., \`https://example.com/llms.txt\`) that provides structured information about the site for consumption by large language models.

Think of it as \`robots.txt\` for the AI era. While \`robots.txt\` tells search engine crawlers what to index, \`llms.txt\` tells AI models what the site is about, what matters most, and where to find key information.

### The Problem It Solves

When an LLM encounters your website (either during training or through retrieval-augmented generation), it must figure out:

1. What is this entity?
2. What are the most important pages?
3. What facts should it know?
4. How should it describe this entity?

Without \`llms.txt\`, the model infers all of this from unstructured HTML — often getting it wrong, using outdated information, or missing key pages.

## Why It Matters

**1. Control your narrative.** LLMs will describe your entity whether you provide guidance or not.

**2. Surface your best content.** Most LLMs and retrieval systems do not crawl every page.

**3. Improve citation accuracy.** When LLMs cite your site, they often get details wrong.

**4. Futureproof discoverability.** As AI interfaces replace traditional search for many queries, having a machine-readable summary becomes as important as having good SEO metadata.

## Quick Start

1. Create a file called \`llms.txt\` in your site's root directory
2. Use the format below (or copy from [templates/](templates/))
3. Deploy it so it's accessible at \`https://yourdomain.com/llms.txt\`
4. Validate it with the [validator tool](tools/validator.py)

## Templates

Ready-to-use templates for different types of organizations:

| Template | Best For |
|---|---|
| [startup.txt](templates/startup.txt) | Early-stage startups and tech companies |
| [ecommerce.txt](templates/ecommerce.txt) | Online stores and retailers |
| [agency.txt](templates/agency.txt) | Marketing, design, and consulting agencies |
| [personal-brand.txt](templates/personal-brand.txt) | Consultants, speakers, authors, experts |
| [saas.txt](templates/saas.txt) | Software-as-a-service products |

## Specification

See [\`spec/llms-txt-spec.md\`](spec/llms-txt-spec.md) for the proposed specification, including:

- File format and encoding
- Required and optional sections
- Linking conventions
- Best practices for content
- Relationship to \`llms-full.txt\`

## Validator

A Python tool for validating \`llms.txt\` files:

\`\`\`bash
python tools/validator.py https://example.com/llms.txt
\`\`\`

The validator checks encoding, required sections, link format, content length, and common mistakes. Requires Python 3.8+ and requests.

## FAQ

**Is llms.txt an official standard?**
Not yet. It is a proposed convention gaining adoption among practitioners.

**Does ChatGPT/Gemini/Perplexity actually read llms.txt?**
RAG systems like Perplexity can access it during real-time retrieval. For training-based models, the file is useful when it appears in training data crawls.

**Should I have both llms.txt and llms-full.txt?**
If your entity is complex, yes. Use llms.txt as a concise summary and llms-full.txt for comprehensive information.

## Citation

\`\`\`
Caramaschi, A. (2026). llms.txt Examples: Templates and Tools for LLM Discoverability. GitHub. https://github.com/alexandrebrt14-sys/llms-txt-templates
\`\`\`

## Related Projects

- [GEO Checklist](https://github.com/alexandrebrt14-sys/geo-checklist) — The most comprehensive open checklist for AI visibility
- [GEO Taxonomy](https://github.com/alexandrebrt14-sys/geo-taxonomy) — Structured vocabulary of 60+ GEO terms and definitions
- [Brasil GEO](https://brasilgeo.ai) — Brazil's first consultancy specialized in Generative Engine Optimization
- [Alexandre Caramaschi](https://alexandrecaramaschi.com) — Full GEO methodology, consulting, and resources

---

## License

MIT License. See [LICENSE](LICENSE).

---

**Author:** [Alexandre Caramaschi](https://alexandrecaramaschi.com) — CEO at Brasil GEO, GEO specialist, ex-CMO Semantix.
