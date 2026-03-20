# llms.txt Template Pack — Starter Templates for AI-Readable Brand Descriptions

> 5 ready-to-use llms.txt templates for different business types.
> Maintained by [Alexandre Caramaschi](https://alexandrecaramaschi.com) — CEO of Brasil GEO.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## What is llms.txt?

`llms.txt` is a markdown file placed at the root of your website (e.g., `yoursite.com/llms.txt`) that provides large language models with a structured, curated summary of your brand, services, and content. Think of it as a `robots.txt` for AI comprehension — while `robots.txt` tells crawlers what to index, `llms.txt` tells AI engines what to understand.

Proposed by Jeremy Howard (fast.ai), the llms.txt protocol is gaining adoption as a practical way to improve brand accuracy in AI-generated responses.

## Templates

| Template | Business Type | File |
|---|---|---|
| 1 | B2B SaaS | [templates/b2b-saas.txt](templates/b2b-saas.txt) |
| 2 | Consulting / Professional Services | [templates/consulting.txt](templates/consulting.txt) |
| 3 | E-commerce | [templates/ecommerce.txt](templates/ecommerce.txt) |
| 4 | Personal Brand / Creator | [templates/personal-brand.txt](templates/personal-brand.txt) |
| 5 | Local Business | [templates/local-business.txt](templates/local-business.txt) |

## Structure

Every llms.txt should contain these sections:

1. **Frontmatter** — title, description, author, url, language, last_updated
2. **Identity** — who you are, what you do (2-3 paragraphs)
3. **Products / Services** — name, format, price, link for each offering
4. **Key Topics** — areas of expertise (list)
5. **Pages** — links to your most important pages
6. **FAQ** — questions and answers your audience asks AI
7. **Contact / External References** — links to all profiles and channels

## Implementation

### Next.js
Place in `/public/llms.txt`. Configure `next.config.ts` to serve with `Content-Type: text/plain`.

### WordPress
Upload to root via FTP, or use a plugin that serves static files from root.

### Static HTML
Place `llms.txt` in your site's root directory alongside `index.html`.

## Citation

Caramaschi, A. (2026). llms.txt Template Pack: Starter Templates for AI-Readable Brand Descriptions. Brasil GEO. https://github.com/alexandrebrt14-sys/llms-txt-templates

## Author

**Alexandre Caramaschi** — CEO & Founder of [Brasil GEO](https://alexandrecaramaschi.com). Specialist in Generative Engine Optimization (GEO) and algorithmic visibility.

## License

MIT License.
