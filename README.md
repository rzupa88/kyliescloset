
# KZ Closet

A kid-friendly closet + outfit planner app (monorepo).

This project is built deliberately in milestones with strong architectural boundaries and small, reviewable PRs.

---

## Monorepo Layout

.
├── services/
│   └── bg/        # Background removal service (FastAPI + rembg)
├── web/           # Front-end application (Next.js - planned)
├── docs/          # Architecture + ADRs
└── docker-compose.yml

---

## Current Status (M1 — Background Removal Service)

We have a working, containerized background removal service:

- `GET /health`
- `POST /remove-bg` → returns transparent PNG (`image/png`)
- Stateless service (returns bytes; does not store files)

### Run Locally

From repo root:

```bash
docker compose up --build

Health check:

curl http://localhost:8000/health

Remove background:

curl -o out.png \
  -F "file=@services/bg/testdata/test.jpg" \
  http://localhost:8000/remove-bg


⸻

Architecture Principles
	•	Services are stateless
	•	Clear separation between:
	•	Image processing (services/bg)
	•	Storage + UI (web)
	•	Docker is the runtime source of truth
	•	Local .venv is editor-only (linting/intellisense)
	•	Every architectural decision is captured as an ADR

⸻

Documentation
	•	Architecture overview: docs/architecture.md
	•	Decisions (ADRs): docs/decisions/
	•	Current milestone: M1 — Background Removal Service

⸻

Project Approach
	•	Milestone-driven development
	•	Small PRs
	•	Explicit acceptance criteria
	•	No premature feature creep
	•	Image pipeline first:

Image → Background Removal → Storage → Render


⸻

CI

Pull requests run CI that:
	•	Ensures repository hygiene
	•	Builds the background service Docker image

