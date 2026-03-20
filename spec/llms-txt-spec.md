# llms.txt Specification (Proposed Draft)

**Version:** 0.1.0
**Date:** March 2026
**Author:** Alexandre Caramaschi
**Status:** Draft — community feedback welcome

---

## 1. Purpose

The llms.txt file provides a structured, plain-text summary of a website or organization, designed for consumption by large language models (LLMs) during training, retrieval, or inference.

## 2. File Location

The file MUST be placed at the root of the domain:

    https://example.com/llms.txt

An optional extended version MAY be placed at:

    https://example.com/llms-full.txt

### 2.1 Relationship Between llms.txt and llms-full.txt

- llms.txt is the concise version (recommended max: 2,000 words)
- llms-full.txt is the extended version (recommended max: 10,000 words)
- If only one file is provided, it SHOULD be llms.txt

## 3. File Format

### 3.1 Encoding

- MUST be UTF-8 encoded plain text
- MUST be served with Content-Type: text/plain; charset=utf-8
- MUST NOT contain HTML tags or JavaScript

### 3.2 Structure

The file uses Markdown-like formatting with headings, blockquotes, and links.

### 3.3 Required Elements

1. **Entity Name** (H1 heading): The canonical name of the entity
2. **Description** (blockquote): A one-to-two sentence factual description

### 3.4 Recommended Sections

| Section | Purpose |
|---|---|
| Overview / About | Extended description, founding date, location, key facts |
| Products / Services | What the entity offers, with links |
| Pricing | Pricing tiers and key terms |
| Team / People | Key individuals with roles |
| Resources | Links to documentation, blog, API, etc. |
| Contact | Website, email, social links |

### 3.5 Content Guidelines

- Content MUST be factual and verifiable
- Content SHOULD be written in third person
- Content MUST NOT contain marketing superlatives
- Content SHOULD include specific numbers over vague claims

## 4. Serving Requirements

- The file MUST be accessible via HTTP GET request
- The server SHOULD return HTTP 200 for a valid file
- The file SHOULD NOT require authentication
- The file SHOULD NOT be blocked by robots.txt

## 5. Discovery

The primary discovery mechanism is direct URL access at the domain root.

Optional discovery hints:
- Reference in robots.txt
- HTML link element in head
- HTTP header (X-LLMs-Txt)

## 6. Relationship to Other Standards

| Standard | Relationship |
|---|---|
| robots.txt | Complementary — controls crawler access vs. provides entity info |
| Schema.org / JSON-LD | Complementary — embedded in HTML vs. standalone summary |
| humans.txt | Analogous pattern |
| security.txt | Analogous pattern |
| XML Sitemap | Complementary — lists all pages vs. highlights important pages |

## 7. Validation

Valid files:
- Are UTF-8 encoded
- Begin with an H1 heading
- Include a blockquote description
- Contain at least one section with content
- Use absolute URLs for all links
- Are under the recommended size limits

---

*Proposed by [Alexandre Caramaschi](https://alexandrecaramaschi.com) — CEO at Brasil GEO.*
