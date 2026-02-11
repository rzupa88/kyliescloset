# Architecture

## Goal
A kid-friendly app to catalog clothes and build outfits + weekly plans. Parent-friendly capture flow.

## Components (planned)
- Web App (`/web`)
  - Closet browsing (big tiles, categories)
  - Outfit builder
  - Weekly planner
- Background Removal Service (`/services/bg`)
  - Accepts an image upload (or later: image URL)
  - Returns a transparent PNG

## Data Flow (planned)
1. Parent adds clothing item image (camera / upload / URL)
2. Background removal runs automatically
3. Clean PNG is stored and used across the app

## Non-goals (MVP)
- AI styling recommendations
- Multi-user accounts
- Public sharing
