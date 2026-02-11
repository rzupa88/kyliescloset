cat > docs/decisions/0001-tech-stack.md << 'EOF'
# ADR 0001 — Tech stack (initial)

## Status
Proposed

## Date
2026-02-11

## Context
We want a Codespaces-friendly build with frequent documentation and small PRs. The MVP must support:
- A kid-friendly visual web UI
- Background removal on import (day 1)
- Simple storage for images + metadata
- Monorepo workflow with milestones/issues/PRs

## Decision (proposed)
- Repo structure: monorepo with `services/`, `web/`, `docs/`
- Development environment: GitHub Codespaces
- Background removal: local open-source solution first (no paid APIs in MVP), exposed as an HTTP service
- Web UI: React-based web app (framework to be decided in a follow-up ADR)
- Storage: to be decided (local-first vs hosted)

## Alternatives considered
- Paid background removal APIs (remove.bg / Photoroom / Clipdrop)
- Native mobile app first
- Separate repos per service/app

## Consequences
- Pro: fast iteration, low/no recurring cost, consistent image pipeline
- Con: local background removal may be less perfect than paid APIs for difficult edges
- Open question: select exact web framework + storage approach next (new ADR)
EOF