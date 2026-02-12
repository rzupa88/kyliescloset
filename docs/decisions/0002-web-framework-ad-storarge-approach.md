# ADR 0002: Choose web framework and storage approach

- **Status:** Accepted
- **Date:** 2026-02-11
- **Owners:** Project maintainers
- **Decision Type:** Architecture / Foundation

## Context

Kylie’s Closet needs a simple, kid-friendly, visual-first UI and a local background-removal pipeline (rembg) that runs in Codespaces without paid APIs.

To implement Milestone M1 (Image → Background Removal → Storage → Render in UI), we must choose:

1. A web framework for the `/web` app.
2. A storage approach for image assets (original + processed).
3. A lightweight MVP data persistence method for listing and tagging items.

We also want:
- Small PRs
- Clear separations between services
- A path to future deployment without rewriting the app

## Decision

### 1) Web framework

We will use **Next.js (TypeScript, App Router)** for the web application in `/web`.

**Why this choice**
- Strong defaults for routing/layouts and future features (upload flows, API routes if needed)
- Easy to deploy later (Vercel or container-based) without major rework
- Works well with a visual, component-driven UI
- Large ecosystem and predictable conventions for teams

### 2) Storage approach

For MVP (M1–M2), we will use **local filesystem storage via Docker volumes**, with a clear directory structure.

- Store **original uploads** and **processed transparent PNGs** as files
- Store **metadata** in a lightweight local DB (see below)
- Use a shared docker volume so services can read/write consistently in Codespaces

This avoids paid storage services and keeps the pipeline simple and debuggable.

### 3) MVP metadata persistence

We will use **SQLite** for MVP metadata storage (e.g., item name, tags, category, laundry status, file paths).

Rationale:
- Zero external dependencies
- Works in Codespaces and local dev reliably
- Easy to migrate to Postgres later if needed

(ORM choice is intentionally deferred; we can use Drizzle or Prisma in a later ADR if it becomes consequential.)

## Options Considered

### Web framework options

#### Option A — Next.js (Chosen)
**Pros**
- App Router + layouts = clean navigation scaffolding
- Easy to grow into (server actions, API routes, auth later if needed)
- Great deployment story

**Cons**
- Slightly more framework complexity than Vite for an empty shell
- Some “fullstack” features we won’t use immediately

#### Option B — Vite + React Router
**Pros**
- Very lightweight and fast dev loop
- Minimal framework opinions

**Cons**
- We’d assemble more of the “app scaffolding” ourselves (routing/layout conventions)
- Future SSR/edge optimizations would be a bigger change if needed

#### Option C — Expo / React Native
**Pros**
- True mobile app experience

**Cons**
- Premature for MVP; adds build/dev complexity and slows M1 pipeline work

---

### Storage options

#### Option A — Local filesystem + Docker volume (Chosen)
**Pros**
- No paid services
- Transparent and easy to debug
- Fast iteration in Codespaces

**Cons**
- Not “cloud-native” by default
- Requires a clean plan for future migration to object storage

#### Option B — Object storage (S3/R2/Supabase Storage)
**Pros**
- Scales and deploys cleanly
- Simplifies serving images in production

**Cons**
- Adds credentials, billing, and integration complexity too early
- Conflicts with “no paid APIs in MVP” principle (even if low-cost)

#### Option C — Store images as DB blobs
**Pros**
- Single persistence layer

**Cons**
- Inefficient, complicates performance/backup, harder to serve images well

---

### Metadata persistence options

#### Option A — SQLite (Chosen)
**Pros**
- Simple, local, reliable
- Great for MVP and demos

**Cons**
- Migration needed later if we outgrow it

#### Option B — Postgres (Supabase)
**Pros**
- Production-grade, scalable
- Strong future path

**Cons**
- Adds infra complexity early; unnecessary for M1

#### Option C — JSON files
**Pros**
- Extremely simple

**Cons**
- Becomes brittle quickly for tagging/filtering/updates

## Consequences

### Positive
- M1 can be built cleanly in Codespaces with minimal dependencies
- Image pipeline stays explicit and easy to troubleshoot
- Web app has a stable foundation for later milestones (Closet, Outfit Builder, Planner)

### Negative / Tradeoffs
- We will need a planned migration path from filesystem to object storage if/when we deploy broadly
- Next.js introduces some framework surface area we won’t use in M1

### Follow-up decisions (explicitly deferred)
- Exact ORM for SQLite (Drizzle vs Prisma) and schema ownership
- Production deployment model (container vs Vercel) and storage migration strategy
- Authentication/parent controls (out of scope until later milestones)

## Implementation Notes (M1)

- Use a shared volume mounted at a stable path (e.g., `/data/kz-closet`)
- The background service will write processed outputs to that volume
- The web app will read from that volume and serve images via a simple local route/proxy

This ADR is intended to unblock M1 work immediately.