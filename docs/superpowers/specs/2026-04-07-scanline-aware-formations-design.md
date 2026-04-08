# Scanline-Aware Formation Coordinate Selection — Design Spec

## Overview

Prevent SNES per-scanline OAM overflow in battle formations by computing each enemy's scanline footprint from sprite mold data and rejecting formation coordinates that would cause graphical corruption. Also bias coordinate selection toward maximum average distance from placed enemies.

## Motivation

The SNES can render at most 32 OAM sprites per scanline. Large non-gridplane enemies (e.g., FROGOG with 19 tiles) can consume ~25 OAM entries at peak scanlines. When two or more overlap vertically, they exceed the limit, causing sprite corruption. The current formation shuffler has no awareness of this — it only checks unique VRAM budget and total distance.

## Scope

- Compute per-enemy scanline OAM footprint from sprite mold tile data
- Validate formation coordinates against per-scanline OAM budget
- Bias coordinate selection toward distance maximization (weighted random)
- Skip adding enemies when no valid coordinate exists

---

## Architecture

### New Module: `randomizer/logic/scanline_calculator.py`

**`get_scanline_footprint(enemy_class, world) -> dict[int, int]`**

Computes the OAM cost per scanline for an enemy sprite, relative to the formation Y coordinate.

1. Load sprite via `monster_id + 256`
2. Get mold 0 (standing pose)
3. For each `Tile` in the mold:
   - Decode signed Y coordinate: `tile.y if tile.y < 128 else tile.y - 256`
   - Count non-None entries in `subtile_bytes[0:2]` → top OAM count (scanlines `tile_y` to `tile_y + 7`)
   - Count non-None entries in `subtile_bytes[2:4]` → bottom OAM count (scanlines `tile_y + 8` to `tile_y + 15`)
   - Accumulate into footprint dict: `{relative_scanline: total_oam_entries}`
4. Cache per enemy type (same enemy = same footprint)

Returns a dict mapping relative scanline offset → OAM entry count at that scanline.

**`find_valid_coordinates(placed_enemies, candidate_footprint, threshold=28) -> list[tuple[int, int]]`**

Filters `VALID_FORMATION_COORDINATES` to those that don't cause any scanline to exceed the OAM threshold.

- `placed_enemies`: list of `(coord, footprint)` tuples for already-placed enemies
- `candidate_footprint`: footprint dict for the enemy being placed
- For each candidate coordinate, compute absolute scanlines by adding formation Y to relative offsets
- Sum OAM entries per absolute scanline across all placed enemies + candidate
- Return coordinates where max scanline OAM <= threshold

### Modified: `randomizer/logic/shufflers/enemies.py`

**`generate_formation_coordinates()`** updated to:

1. Accept enemy types and world reference (to compute footprints)
2. For each enemy to place:
   - Compute scanline footprint via `get_scanline_footprint`
   - Get valid coordinates via `find_valid_coordinates`
   - If no valid coordinates exist, signal that this enemy can't be placed (return fewer coordinates)
   - Among valid coordinates, weight by average Euclidean distance to already-placed coordinates (biased random, not deterministic max)
3. The caller (`randomize_enemy_formations`) uses the returned coordinate count to trim the enemy list if needed

### Distance-Biased Selection

Instead of pure random or deterministic max-distance:
- Compute average Euclidean distance from each valid coordinate to all already-placed coordinates
- Use distances as weights for `random.choices` (higher distance = higher probability)
- First enemy: uniform random from all valid coordinates

---

## Constants

- `OAM_SCANLINE_THRESHOLD = 28` — max OAM entries per scanline (32 hardware limit minus ~4 for player sprites)

## Edge Cases

- **Clone tiles**: Skip any tile where `is_clone=True` (clones reference parent tile data, handled separately)
- **Gridplane sprites**: Still compute footprint from tiles, but tile dimensions differ by format. For gridplane tiles, the subtile arrangement may be 3x3 or 4x4 rather than 2x2. Use the gridplane format to determine the correct scanline range per tile.
- **Empty subtile_bytes**: A Tile with all-None subtile_bytes contributes 0 OAM entries
- **Single enemy exceeds threshold alone**: Allowed (single large enemies work fine in vanilla). The threshold only applies to the sum across all enemies on a scanline.

## Files

| File | Action | Responsibility |
|------|--------|----------------|
| `randomizer/logic/scanline_calculator.py` | Create | Footprint computation + coordinate validation |
| `randomizer/logic/shufflers/enemies.py` | Modify | Integrate scanline check into coordinate selection, distance-biased weighting |
