# Architecture

## Product goal
A kid-friendly “closet” app that lets a parent capture clothing items (photo or online image), automatically remove the background, and help a child build outfits and plan a week (school, activities, lounge, pajamas).

## Users
- Child (primary): browses closet, likes outfits, builds outfits with big visuals
- Parent (admin): captures items, tags items, manages laundry/availability

## Principles
- Visual-first UI (minimal reading required)
- Small, shippable milestones
- Background removal is automatic on import (day 1)
- Store processed images we control (avoid broken external links)

## System overview (MVP)
- Web App (`/web`)
  - Closet: browse items by category
  - Outfit builder: combine items into an outfit
  - Weekly planner: assign outfits to days and occasions
- Background Removal Service (`/services/bg`)
  - Input: image upload (file)
  - Output: transparent PNG
- Storage (chosen later)
  - Stores item metadata + images

## Data model (initial)
### ClothingItem
- id
- name (optional; parent-facing)
- category (top, bottom, dress, outerwear, shoes, pajamas, accessory)
- tags (school, play, fancy, sport, lounge, pajamas)
- comfort (comfy | fancy)
- season (winter | spring | summer | fall) (optional)
- status (available | in_laundry)
- image:
  - original_source (camera | upload | url)
  - processed_png_url (stored asset)

### Outfit
- id
- name (optional)
- items[] (references ClothingItem)
- tags (school, play, fancy, sport, lounge, pajamas)
- favorite (boolean)

### PlanDay
- date
- occasions[]:
  - occasion_type (school | activity | weekend | lounge | pajamas)
  - outfit_id

## Key flows
### Import clothing item (parent)
1. Parent adds photo/upload/URL
2. Background removal runs
3. Processed PNG stored
4. Parent applies category + tags
5. Item appears in closet

### Shuffle / outfit creation (child)
1. App suggests an outfit (or child builds one)
2. Child taps 👍 👎 💖
3. Favorites are easy to re-use

### Weekly planning (parent + child)
1. Select a week
2. Drag outfits onto days/occasions
3. Morning view shows “today’s outfit” with big visuals

## Non-goals (MVP)
- Public accounts / social sharing
- AI-based style recommendations
- Multi-device sync across families
