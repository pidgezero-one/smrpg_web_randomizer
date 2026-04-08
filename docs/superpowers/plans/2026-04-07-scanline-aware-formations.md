# Scanline-Aware Formation Coordinate Selection Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Prevent SNES per-scanline OAM overflow in battle formations by computing sprite scanline footprints and rejecting coordinates that would cause graphical corruption.

**Architecture:** A new `scanline_calculator.py` module computes per-enemy OAM footprints from sprite mold tile data. The existing `generate_formation_coordinates()` in `enemies.py` is modified to accept enemy types, filter coordinates by scanline budget, and bias selection toward maximum distance using weighted random.

**Tech Stack:** Python, sprite data from `randomizer/data/sprites/objects/`

---

## File Structure

| File | Action | Responsibility |
|------|--------|----------------|
| `randomizer/logic/scanline_calculator.py` | Create | Scanline footprint computation + coordinate validation |
| `randomizer/logic/shufflers/enemies.py` | Modify | Integrate scanline checks into coordinate selection and formation building |

---

### Task 1: Scanline Footprint Calculator

**Files:**
- Create: `randomizer/logic/scanline_calculator.py`

This module computes how many OAM entries an enemy sprite contributes to each scanline, relative to its formation Y coordinate.

- [ ] **Step 1: Create `randomizer/logic/scanline_calculator.py`**

```python
"""Scanline-aware OAM budget calculator for battle formations.

Computes per-enemy scanline footprints from sprite mold tile data.
Used by the formation shuffler to prevent SNES per-scanline OAM overflow.

SNES hardware limits per scanline:
- 32 OAM sprite entries
- 34 character tiles (8x8 units)

Each non-None subtile in a sprite mold tile corresponds to one 8x8 OAM entry.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld

# Max OAM entries per scanline. 32 is the SNES hardware limit;
# 28 leaves headroom for ~4 player character OAM entries.
OAM_SCANLINE_THRESHOLD = 28

# Cache footprints per sprite ID to avoid recomputation
_footprint_cache: dict[int, dict[int, int]] = {}


def _compute_footprint_non_gridplane(tiles: list) -> dict[int, int]:
    """Compute scanline footprint for a non-gridplane (metasprite) mold.

    Each tile is a 16x16 area positioned at (tile.x, tile.y) with up to 4
    subtiles in a 2x2 grid of 8x8 OAM sprites:
      indices 0,1 = top row (y to y+7)
      indices 2,3 = bottom row (y+8 to y+15)

    Each non-None subtile = 1 OAM entry on its 8-scanline range.
    """
    footprint: dict[int, int] = {}

    for tile in tiles:
        if hasattr(tile, 'is_clone') and tile.is_clone:
            continue

        subtile_bytes = getattr(tile, 'subtile_bytes', None)
        if not subtile_bytes:
            continue

        # Decode signed Y coordinate
        raw_y = tile.y
        tile_y = raw_y if raw_y < 128 else raw_y - 256

        # Top row: subtile_bytes[0:2], scanlines tile_y to tile_y+7
        top_oam = sum(1 for s in subtile_bytes[0:2] if s is not None)
        if top_oam > 0:
            for scanline in range(tile_y, tile_y + 8):
                footprint[scanline] = footprint.get(scanline, 0) + top_oam

        # Bottom row: subtile_bytes[2:4], scanlines tile_y+8 to tile_y+15
        bottom_oam = sum(1 for s in subtile_bytes[2:4] if s is not None)
        if bottom_oam > 0:
            for scanline in range(tile_y + 8, tile_y + 16):
                footprint[scanline] = footprint.get(scanline, 0) + bottom_oam

    return footprint


def _compute_footprint_gridplane(tile, format_val: int) -> dict[int, int]:
    """Compute scanline footprint for a gridplane mold.

    Gridplane sprites have a single tile with subtiles arranged in a grid.
    The format determines columns per row:
      format 0-1: 4 columns (FOUR_SPRITES_PER_ROW)
      format 2-3: 3 columns (THREE_SPRITES_PER_ROW)

    Each non-None subtile = 1 OAM entry. Subtiles are ordered left-to-right,
    top-to-bottom. Each row covers 8 scanlines.
    """
    subtile_bytes = getattr(tile, 'subtile_bytes', None)
    if not subtile_bytes:
        return {}

    cols = 4 if format_val <= 1 else 3
    raw_y = tile.y
    tile_y = raw_y if raw_y < 128 else raw_y - 256

    footprint: dict[int, int] = {}
    for idx, subtile in enumerate(subtile_bytes):
        if subtile is None:
            continue
        row = idx // cols
        row_y_start = tile_y + (row * 8)
        for scanline in range(row_y_start, row_y_start + 8):
            footprint[scanline] = footprint.get(scanline, 0) + 1

    return footprint


def get_scanline_footprint(enemy_type: type, world: GameWorld) -> dict[int, int]:
    """Get the OAM-per-scanline footprint for an enemy sprite.

    Returns a dict mapping relative scanline offset -> OAM entry count.
    Results are cached per sprite ID.

    Args:
        enemy_type: The enemy class (has monster_id attribute).
        world: The game world (for sprite access).

    Returns:
        Dict of {relative_scanline: oam_count}.
    """
    enemy = world.enemies.get_by_type(enemy_type)
    sprite_id = enemy.monster_id + 256

    if sprite_id in _footprint_cache:
        return _footprint_cache[sprite_id]

    try:
        sprite = world.get_sprite(sprite_id)
        mold = sprite.animation.properties.molds[0]
    except (IndexError, AttributeError):
        _footprint_cache[sprite_id] = {}
        return {}

    if mold.gridplane:
        # Gridplane: single tile with grid-arranged subtiles
        if mold.tiles:
            tile = mold.tiles[0]
            format_val = tile.format if hasattr(tile, 'format') else 0
            footprint = _compute_footprint_gridplane(tile, format_val)
        else:
            footprint = {}
    else:
        # Non-gridplane (metasprite): multiple positioned tiles
        footprint = _compute_footprint_non_gridplane(mold.tiles)

    _footprint_cache[sprite_id] = footprint
    return footprint


def check_scanline_budget(
    placed_enemies: list[tuple[tuple[int, int], dict[int, int]]],
    candidate_coord: tuple[int, int],
    candidate_footprint: dict[int, int],
    threshold: int = OAM_SCANLINE_THRESHOLD,
) -> bool:
    """Check if placing a candidate enemy at a coordinate stays within OAM budget.

    Args:
        placed_enemies: List of ((x, y), footprint) for already-placed enemies.
        candidate_coord: The (x, y) coordinate to test for the candidate.
        candidate_footprint: The scanline footprint of the candidate enemy.
        threshold: Maximum OAM entries allowed per scanline.

    Returns:
        True if no scanline exceeds the threshold.
    """
    # Build absolute scanline -> OAM count from already placed enemies
    scanline_oam: dict[int, int] = {}
    for (_, placed_y), footprint in placed_enemies:
        for rel_scanline, oam_count in footprint.items():
            abs_scanline = placed_y + rel_scanline
            scanline_oam[abs_scanline] = scanline_oam.get(abs_scanline, 0) + oam_count

    # Add candidate's contribution
    _, candidate_y = candidate_coord
    for rel_scanline, oam_count in candidate_footprint.items():
        abs_scanline = candidate_y + rel_scanline
        total = scanline_oam.get(abs_scanline, 0) + oam_count
        if total > threshold:
            return False

    return True


def find_valid_coordinates(
    placed_enemies: list[tuple[tuple[int, int], dict[int, int]]],
    candidate_footprint: dict[int, int],
    valid_coordinates: list[tuple[int, int]],
    threshold: int = OAM_SCANLINE_THRESHOLD,
) -> list[tuple[int, int]]:
    """Filter coordinates to those that don't exceed the scanline OAM budget.

    Args:
        placed_enemies: List of ((x, y), footprint) for already-placed enemies.
        candidate_footprint: The scanline footprint of the candidate enemy.
        valid_coordinates: All possible formation coordinates.
        threshold: Maximum OAM entries allowed per scanline.

    Returns:
        List of valid (x, y) coordinates.
    """
    return [
        coord for coord in valid_coordinates
        if check_scanline_budget(placed_enemies, coord, candidate_footprint, threshold)
    ]
```

- [ ] **Step 2: Verify the module loads and computes FROGOG footprint**

```bash
cd /Users/stefkischak/code/smrpg_web_randomizer && python -c "
from randomizer.logic.scanline_calculator import _compute_footprint_non_gridplane
from randomizer.data.sprites.objects.sprite_305 import sprite

mold = sprite.animation.properties.molds[0]
footprint = _compute_footprint_non_gridplane(mold.tiles)

# Find peak scanline
peak = max(footprint.values())
peak_scanlines = [s for s, c in footprint.items() if c == peak]
print(f'FROGOG: {len(footprint)} scanlines covered, peak OAM={peak} at scanlines {peak_scanlines[:3]}...')
print(f'Total scanline range: {min(footprint.keys())} to {max(footprint.keys())}')

# Check: 3 FROGOGs at closest coordinates should exceed threshold
from randomizer.logic.scanline_calculator import check_scanline_budget
coords = [(135, 111), (135, 127), (135, 143)]
placed = []
for i, coord in enumerate(coords):
    if i > 0:
        ok = check_scanline_budget(placed, coord, footprint)
        print(f'FROGOG {i+1} at {coord}: valid={ok}')
    placed.append((coord, footprint))
"
```

Expected: FROGOG has a large footprint. Third FROGOG at a close coordinate should be rejected (valid=False).

- [ ] **Step 3: Commit**

```bash
git add randomizer/logic/scanline_calculator.py
git commit -m "Add scanline OAM budget calculator for battle formations"
```

---

### Task 2: Integrate Scanline Checks into Formation Coordinate Selection

**Files:**
- Modify: `randomizer/logic/shufflers/enemies.py:338-404` (coordinate functions)
- Modify: `randomizer/logic/shufflers/enemies.py:527-569` (formation building loop)

The existing `generate_formation_coordinates()` is replaced with a scanline-aware version that accepts enemy types and filters coordinates. The formation building loop is updated to skip enemies that can't fit.

- [ ] **Step 1: Update `generate_formation_coordinates` signature and logic**

In `randomizer/logic/shufflers/enemies.py`, replace the existing `generate_formation_coordinates` function (lines 369-404) with:

```python
def generate_formation_coordinates(
    enemy_types: list[type],
    world: GameWorld,
    valid_coordinates: list[tuple[int, int]] | None = None,
) -> list[tuple[int, int] | None]:
    """Generate scanline-safe, distance-biased formation coordinates.

    For each enemy, filters valid coordinates by scanline OAM budget,
    then selects using distance-weighted random (biased toward spreading out,
    but not deterministic).

    Args:
        enemy_types: Ordered list of enemy types to place.
        world: The game world (for sprite access).
        valid_coordinates: Optional override for valid positions.

    Returns:
        List of (x, y) tuples, one per enemy. None if enemy can't fit.
    """
    from randomizer.logic.scanline_calculator import (
        get_scanline_footprint,
        find_valid_coordinates,
    )

    if valid_coordinates is None:
        valid_coordinates = VALID_FORMATION_COORDINATES

    if not enemy_types:
        return []

    result: list[tuple[int, int] | None] = []
    placed_enemies: list[tuple[tuple[int, int], dict[int, int]]] = []

    for enemy_type in enemy_types:
        footprint = get_scanline_footprint(enemy_type, world)

        # Filter coordinates by scanline budget
        valid = find_valid_coordinates(
            placed_enemies, footprint, valid_coordinates
        )

        if not valid:
            result.append(None)
            continue

        if not placed_enemies:
            # First enemy: uniform random
            coord = random.choice(valid)
        else:
            # Subsequent: distance-weighted random
            used_coords = [c for c, _ in placed_enemies]
            weights = [
                _get_collective_distance(c[0], c[1], used_coords)
                for c in valid
            ]
            # Avoid zero weights
            if all(w == 0 for w in weights):
                coord = random.choice(valid)
            else:
                coord = random.choices(valid, weights=weights, k=1)[0]

        result.append(coord)
        placed_enemies.append((coord, footprint))

    return result
```

- [ ] **Step 2: Update the formation building loop to handle None coordinates**

In `randomizer/logic/shufflers/enemies.py`, find the section that builds formations (around lines 559-569):

```python
            random.shuffle(chosen_enemies)

            coordinates = generate_formation_coordinates(len(chosen_enemies))

            new_members: list[FormationMember | None] = []
            for enemy_type, (x, y) in zip(chosen_enemies, coordinates):
                new_members.append(
                    FormationMember(enemy=enemy_type, x_pos=x, y_pos=y, hidden_at_start=False)
                )

            formation.set_members(new_members)
```

Replace with:

```python
            random.shuffle(chosen_enemies)

            coordinates = generate_formation_coordinates(chosen_enemies, world)

            new_members: list[FormationMember | None] = []
            for enemy_type, coord in zip(chosen_enemies, coordinates):
                if coord is None:
                    continue  # Skip enemies that can't fit on scanline budget
                x, y = coord
                new_members.append(
                    FormationMember(enemy=enemy_type, x_pos=x, y_pos=y, hidden_at_start=False)
                )

            # Ensure at least one enemy in formation
            if not new_members:
                # Fallback: place just the first enemy at a random coord
                x, y = random.choice(VALID_FORMATION_COORDINATES)
                new_members.append(
                    FormationMember(enemy=chosen_enemies[0], x_pos=x, y_pos=y, hidden_at_start=False)
                )

            formation.set_members(new_members)
```

- [ ] **Step 3: Add the import for GameWorld at the top of enemies.py**

At the top of `randomizer/logic/shufflers/enemies.py`, verify `GameWorld` is imported. It should already be available since the function `randomize_enemy_formations` takes `world: GameWorld` as a parameter. If not imported, add:

```python
from randomizer.types.gameworld import GameWorld
```

- [ ] **Step 4: Verify end-to-end with FROGOG test**

```bash
cd /Users/stefkischak/code/smrpg_web_randomizer && python -c "
from randomizer.logic.scanline_calculator import get_scanline_footprint, find_valid_coordinates, OAM_SCANLINE_THRESHOLD
from randomizer.logic.shufflers.enemies import VALID_FORMATION_COORDINATES

# Simulate placing 3 FROGOGs
from randomizer.data.sprites.objects.sprite_305 import sprite
from randomizer.logic.scanline_calculator import _compute_footprint_non_gridplane

mold = sprite.animation.properties.molds[0]
frogog_footprint = _compute_footprint_non_gridplane(mold.tiles)

placed = []
for i in range(3):
    valid = find_valid_coordinates(placed, frogog_footprint, VALID_FORMATION_COORDINATES)
    print(f'FROGOG {i+1}: {len(valid)} valid coords out of {len(VALID_FORMATION_COORDINATES)}')
    if valid:
        import random
        coord = random.choice(valid)
        placed.append((coord, frogog_footprint))
        print(f'  Placed at {coord}')
    else:
        print(f'  Cannot place — scanline budget exceeded')

print(f'Total placed: {len(placed)}/{3}')
"
```

Expected: First FROGOG places freely (9 valid coords). Second has fewer options. Third may or may not fit depending on Y spread. If it can't fit, that's the correct behavior preventing the glitch.

- [ ] **Step 5: Commit**

```bash
git add randomizer/logic/shufflers/enemies.py
git commit -m "Integrate scanline-aware coordinate selection into formation shuffler"
```

---

### Task 3: Clear Footprint Cache Between Seeds

**Files:**
- Modify: `randomizer/logic/scanline_calculator.py`
- Modify: `randomizer/logic/shufflers/enemies.py`

The footprint cache uses module-level state. Clear it at the start of each formation shuffle to prevent stale data across seeds (e.g., when running the web server).

- [ ] **Step 1: Add cache-clearing function**

In `randomizer/logic/scanline_calculator.py`, add after the cache declaration:

```python
def clear_footprint_cache() -> None:
    """Clear the cached footprints. Call at the start of each seed generation."""
    _footprint_cache.clear()
```

- [ ] **Step 2: Call it at the start of `randomize_enemy_formations`**

In `randomizer/logic/shufflers/enemies.py`, at the beginning of `randomize_enemy_formations()` (after the docstring), add:

```python
    from randomizer.logic.scanline_calculator import clear_footprint_cache
    clear_footprint_cache()
```

- [ ] **Step 3: Commit**

```bash
git add randomizer/logic/scanline_calculator.py randomizer/logic/shufflers/enemies.py
git commit -m "Clear scanline footprint cache between seed generations"
```
