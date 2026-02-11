# ADR 0001 — Tech stack (initial)

## Status
Proposed

## Context
We want a Codespaces-friendly monorepo, fast iteration, and a simple path to a private family app.

## Decision (proposed)
- Monorepo structure: `services/` + `web/` + `docs/`
- Background removal: local open-source approach first (no paid APIs in MVP)
- Web UI: React-based (final selection in a later ADR)

## Consequences
- We prioritize reliable developer experience and documentation cadence over early polish.
