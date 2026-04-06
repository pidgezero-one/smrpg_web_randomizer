# Prize Offset Slider — Design Spec

## Overview

A dev-only UI feature that provides a slider controlling deterministic placement of boss fight prizes, slot machine prizes, and invisible flag locations. This replaces manual config.yml editing for these three prize categories, enabling rapid iteration when testing prize placement across the game world.

## Motivation

Currently, testing specific boss fight / slot / invisible flag placements requires manually editing `config.yml` entries. This feature lets a developer slide through all 47 possible rotations and instantly preview what goes where, then generate a seed with those placements applied.

## Scope

- One slider (0-46) with an enable/disable toggle
- Real-time preview of all assignments
- Backend application of offset at randomization time
- Dev-only (behind `debug_enabled` gate)

---

## Architecture

### Ordered List Provider

**Location:** New function(s) in `randomizer/debug/__init__.py` (or a new module `randomizer/debug/offset_preview.py`).

**`get_ordered_lists()`** returns four ordered lists as class references:

1. **Boss locations** (47 items) — All `BossFightLocation` and `MimicFightLocation` subclasses from `prizelocations.py`, in definition order.
2. **Boss prizes** (47 items) — All `BossFightPrize` subclasses from `prizes.py`, in definition order.
3. **Eligible chest rooms** — All `TreasureChestLocationRow` subclasses where `SlotsPrize` is not in `_blacklist`, deduplicated to one per room (first encountered in definition order wins), ordered by definition.
4. **Invisible flag locations** — All `InvisibleFlagLocation` subclasses from `prizelocations.py`, in definition order.

**`compute_offset_assignments(offset: int)`** returns a dict with:

- `bosses`: list of `(location_class_name, prize_class_name)` — `location[i]` gets `prize[(i + offset) % 47]`
- `slots`: list of 3 `(chest_class_name, slots_prize_name)` — starting at `(offset * 3) % len(eligible_chests)`, wrapping around
- `flags`: list of 3 `flag_class_name` — starting at `(3 * offset) % len(flag_locations)`, wrapping around

Both the Django view (for JSON embedding) and the randomization backend call these same functions — single source of truth.

### Frontend

**Location:** `randomizer/templates/randomizer/_rom_settings.html`, inside the existing `{% if debug_enabled %}` block.

**Controls:**
- Checkbox/toggle to enable prize offset (default: off)
- Range slider (0-46), only visible when toggle is on
- Current offset value displayed next to slider
- State persisted to localStorage (like `debug_mode`)

**Preview table** (visible when toggle is on):
- **Boss fights** — 47 rows, two columns: Location name → Prize name
- **Slot machines** — 3 rows: Chest room name → SlotsPrize1/2/3
- **Invisible flags** — 3 rows: Flag location names

Names displayed as raw class names (dev-only tool, no prettification needed).

**Data source:** Django view embeds the four ordered lists as JSON arrays of class name strings in the template. JavaScript computes assignments client-side using the same modular arithmetic as the backend, updating the preview on every slider input event.

### Backend — Applying the Offset

**Views (`randomizer/views.py`):**
- Accept `prize_offset` as a form parameter alongside `debug_mode`
- Value is `null`/absent when toggle is off; integer 0-46 when enabled
- Pass through to the Settings object or debug config path

**Prize location setup (`randomizer/logic/setup/prize_locations.py`):**
- When `debug_mode` is on and `prize_offset` is not null:
  - Call `compute_offset_assignments(offset)`
  - Feed boss fight assignments into the existing pre-placement/override mechanism (same path config.yml's `items.override` uses)
  - Place SlotsPrize1/2/3 into the computed chest rooms via the same mechanism
  - Set the 3 invisible flag locations, overriding both config.yml's `invisible_flags` and the random selection
  - All offset-placed items are recognized as pre-placed by the shuffler (extending existing config.yml pre-placement logic)
- When `prize_offset` is null/disabled: existing config.yml behavior applies unchanged

**Config.yml interaction:**
- Offset enabled: boss fights, slots, and invisible flags are determined by the offset. Any config.yml settings for those categories are ignored.
- Offset disabled: config.yml applies normally.
- Non-colliding config.yml settings (`starting_coins`, `starting_frog_coins`, `items.start`, non-boss/slot/flag overrides) always apply regardless.

---

## Data Flow

```
Page Load:
  Django view
    → calls get_ordered_lists()
    → serializes to JSON
    → embeds in template context

User Interaction:
  Toggle on → slider appears (0-46)
  Slider drag → JS reads embedded JSON lists
               → computes assignments with modular arithmetic
               → updates preview table

Form Submit:
  prize_offset sent as form param (null if toggle off)
    → views.py passes to Settings/debug config
    → prize_locations.py calls compute_offset_assignments(offset)
    → results fed into existing pre-placement mechanism
    → shuffler sees them as pre-placed, skips them
```

## Edge Cases

- **Wrapping:** Eligible chest rooms and invisible flag locations have fewer than 47*3 entries. Selection wraps around using modulo when offset is high.
- **Offset 0 vs. off:** Offset 0 is a meaningful value (vanilla ordering). "Off" means the feature is disabled entirely and config.yml applies normally.
- **47:47 boss mapping:** 47 boss locations and 47 boss prizes — offset always produces a valid 1:1 mapping via modular rotation.

## Files Modified

| File | Change |
|------|--------|
| `randomizer/debug/__init__.py` (or new module) | `get_ordered_lists()`, `compute_offset_assignments()` |
| `randomizer/templates/randomizer/_rom_settings.html` | Slider UI, toggle, preview table, JS logic |
| `randomizer/views.py` | Accept `prize_offset` param, pass to settings |
| `randomizer/logic/setup/prize_locations.py` | Apply offset assignments via existing pre-placement path |
