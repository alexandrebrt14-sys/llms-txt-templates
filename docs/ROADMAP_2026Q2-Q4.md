# Roadmap 2026 Q2-Q3-Q4 — llms-txt-templates

> Fonte: [`.cto/review-2026-05-04-masterplan-15-repos.md`](.cto/review-2026-05-04-masterplan-15-repos.md) e `planoCTO.html` (913 linhas).
> Próxima revisão CTO: **2026-08-01**.
> Owner: **Alexandre Caramaschi**.

## Sumário

- **Categoria:** spec-publica
- **Criticidade:** baixa
- **Deadline principal do trimestre:** 2026-09-15 (versao 2026.2)
- **Gates obrigatórios:** —

## Decisões pendentes do owner

_Nenhuma decisão pendente listada na auditoria CTO de 2026-05-04._

## Q2 2026 (mai-jun-jul) — janelas críticas

_Sem ondas planejadas para Q2 2026._

## Q3 2026 (ago-set-out) — consolidação e infraestrutura

| ID | Janela | Esforço (h) | Owner | Critical path | Saída esperada | Pré-requisitos |
|---|---|---|---|---|---|---|
| Q3-W5-companion | 01-09 a 15-09 | 10 | Alexandre | Não | Versao 2026.2 com novos templates AEO | — |

## Q4 2026 (nov-dez-jan/27) — captação 2027.1 + colheita

_Sem ondas planejadas para Q4 2026._

## Observabilidade

GitHub stars, validator runs, downloads.

## Política de qualidade

Toda mudança neste repo passa pelos gates transversais aplicáveis:

- **Quality gate canônico** (Next.js/TS): `tsc` + `lint` + `vitest` + `next build` antes de push.
- **Voice Guard** (conteúdo Alexandre): `python scripts/python/voice_guard.py check --file ...` antes de publicar.
- **Migration gate pt_br** (SQL): grep de acentos obrigatório antes de `apply` via Management API.
- **Pre-commit hook** (todo repo cliente): `secret_guard` ativo via `git config core.hooksPath .githooks`.
- **Snapshot Shopify** (mutations produto/variant): JSON em `data/raw/shopify-audit-logs/` antes de `productUpdate`/`variantsBulkUpdate`.
- **Browser MCP visual double-check** (mudanças de UI): `getComputedStyle` antes/depois em 1440x900 e 390x844.
- **Schema.org JSON-LD** (todo conteúdo público): validação com `validate_graphql_codeblocks` ou Rich Results.

## Disciplina de deploy

- `landing-page-geo` no Vercel: máximo **2 pushes/dia** (build minutes ~$0,26/push).
- Pre-push hook roda `next build` localmente; falhar localmente = abortar push.
- Janelas com 2+ streams paralelos exigem revisão semanal de carga em segunda 09h BRT.

## FinOps

- LLM API spend rastreado em [`geo-finops/calls.db`](https://github.com/alexandre-/geo-finops).
- Build minutes Vercel monitorados; alertas WhatsApp/email em ≥80% da quota.
- Quebrar prompts no orchestrator: `< 5KB` input e `< 30KB` output (limite Gemini MAX_TOKENS).

## Política de revisão

- Toda decisão arquitetural significativa registrada como ADR em `docs/adr/`.
- Drift entre `adminalexandre` e `landing-page-geo`: pre-commit hook (deadline 20-05).
- Revisão CTO trimestral próxima: **2026-08-01**.

---

_Gerado automaticamente pela skill `/cto` em 2026-05-04 a partir do masterplan dos 15 repositórios._
