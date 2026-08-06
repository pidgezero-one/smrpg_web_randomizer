"""Scanline footprint calculator for SMRPG battle formations.

Computes how many OAM entries an enemy sprite contributes to each scanline,
relative to its formation Y coordinate. The SNES can render at most 32 OAM
sprites per scanline. When large enemies overlap vertically in battle, they
exceed this limit causing graphical corruption.

Threshold is 28 (leaving 4 for player sprites and effects).
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from smrpgpatchbuilder.datatypes.graphics.classes import Clone, Mold, Tile

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld

# Leave 4 OAM slots for player sprites and battle effects
OAM_SCANLINE_THRESHOLD = 28

# Module-level cache: sprite_id -> {relative_scanline: oam_count}
_footprint_cache: dict[int, dict[int, int]] = {}


def _compute_footprint_non_gridplane(tiles: list[Tile | Clone]) -> dict[int, int]:
    """Compute OAM scanline footprint for a non-gridplane (metasprite) mold.

    Each tile is a 16x16 area at position (tile.x, tile.y) containing up to 4
    subtiles in a 2x2 grid of 8x8 OAM sprites:
      - subtile_bytes indices 0, 1 = top row (scanlines tile_y to tile_y+7)
      - subtile_bytes indices 2, 3 = bottom row (scanlines tile_y+8 to tile_y+15)

    tile.y uses signed byte encoding: values >= 128 mean negative (tile.y - 256).
    Each non-None subtile = 1 OAM entry.
    Skip tiles where is_clone is True.

    Returns:
        Dict mapping relative scanline to total OAM entry count.
    """
    footprint: dict[int, int] = {}

    for tile in tiles:
        if isinstance(tile, Clone) or tile.is_clone:
            continue

        # Signed byte encoding for y
        tile_y = tile.y if tile.y < 128 else tile.y - 256

        subtiles = tile.subtile_bytes

        # Count non-None subtiles in top row (indices 0, 1)
        top_count = sum(1 for i in (0, 1) if i < len(subtiles) and subtiles[i] is not None)

        # Count non-None subtiles in bottom row (indices 2, 3)
        bottom_count = sum(1 for i in (2, 3) if i < len(subtiles) and subtiles[i] is not None)

        # Top row covers scanlines tile_y to tile_y+7
        if top_count > 0:
            for scanline in range(tile_y, tile_y + 8):
                footprint[scanline] = footprint.get(scanline, 0) + top_count

        # Bottom row covers scanlines tile_y+8 to tile_y+15
        if bottom_count > 0:
            for scanline in range(tile_y + 8, tile_y + 16):
                footprint[scanline] = footprint.get(scanline, 0) + bottom_count

    return footprint


def _compute_footprint_gridplane(tile: Tile, format_val: int) -> dict[int, int]:
    """Compute OAM scanline footprint for a gridplane sprite.

    Gridplane sprites have a single tile with subtiles arranged in a grid:
      - format 0, 1: 3 columns per row
      - format 2, 3: 4 columns per row

    Subtiles are ordered left-to-right, top-to-bottom.
    Row N covers scanlines tile_y + (N*8) to tile_y + (N*8) + 7.
    Each non-None subtile in a row = 1 OAM entry on those scanlines.

    Returns:
        Dict mapping relative scanline to total OAM entry count.
    """
    # Signed byte encoding for y
    tile_y = tile.y if tile.y < 128 else tile.y - 256

    if format_val in (0, 1):
        cols = 3
    else:
        cols = 4

    subtiles = tile.subtile_bytes
    num_rows = (len(subtiles) + cols - 1) // cols
    footprint: dict[int, int] = {}

    for row in range(num_rows):
        # Count non-None subtiles in this row
        row_start = row * cols
        row_end = min(row_start + cols, len(subtiles))
        oam_count = sum(1 for i in range(row_start, row_end) if subtiles[i] is not None)

        if oam_count > 0:
            scanline_start = tile_y + (row * 8)
            for scanline in range(scanline_start, scanline_start + 8):
                footprint[scanline] = footprint.get(scanline, 0) + oam_count

    return footprint


def get_scanline_footprint(enemy_type: type, world: GameWorld) -> dict[int, int]:
    """Get the scanline footprint for an enemy type.

    Computes the OAM entries per relative scanline for the enemy's sprite
    (mold 0, the standing/idle pose).

    Args:
        enemy_type: The enemy class type.
        world: The game world instance for sprite lookups.

    Returns:
        Dict mapping relative scanline to OAM entry count.
    """
    enemy = world.enemies.get_by_type(enemy_type)
    sprite_id = int(enemy.monster_id) + 256

    if sprite_id in _footprint_cache:
        return _footprint_cache[sprite_id]

    sprite = world.get_sprite(sprite_id)
    mold: Mold = sprite.animation.properties.molds[0]

    if mold.gridplane:
        tile = mold.tiles[0]
        if isinstance(tile, Clone):
            _footprint_cache[sprite_id] = {}
            return {}
        footprint = _compute_footprint_gridplane(tile, tile.format)
    else:
        footprint = _compute_footprint_non_gridplane(mold.tiles)

    _footprint_cache[sprite_id] = footprint
    return footprint


def check_scanline_budget(
    placed_enemies: list[tuple[tuple[int, int], dict[int, int]]],
    candidate_coord: tuple[int, int],
    candidate_footprint: dict[int, int],
    threshold: int = OAM_SCANLINE_THRESHOLD,
) -> bool:
    """Check whether placing a candidate enemy would exceed the OAM scanline budget.

    Args:
        placed_enemies: List of ((x, y), footprint) tuples for already-placed enemies.
        candidate_coord: The (x, y) coordinate for the candidate enemy.
        candidate_footprint: The scanline footprint dict for the candidate enemy.
        threshold: Max OAM entries per scanline (default 28).

    Returns:
        True if no scanline exceeds the threshold, False otherwise.
    """
    # Accumulate OAM per absolute scanline
    scanline_totals: dict[int, int] = {}

    # Add placed enemies
    for (_, formation_y), footprint in placed_enemies:
        for rel_scanline, oam_count in footprint.items():
            abs_scanline = formation_y + rel_scanline
            scanline_totals[abs_scanline] = scanline_totals.get(abs_scanline, 0) + oam_count

    # Add candidate
    _, candidate_y = candidate_coord
    for rel_scanline, oam_count in candidate_footprint.items():
        abs_scanline = candidate_y + rel_scanline
        scanline_totals[abs_scanline] = scanline_totals.get(abs_scanline, 0) + oam_count

    # Check threshold
    for total in scanline_totals.values():
        if total > threshold:
            return False
    return True


def _footprint_range(
    coord: tuple[int, int], footprint: dict[int, int]
) -> tuple[int, int] | None:
    """Return the (min_abs_scanline, max_abs_scanline) covered by a placed enemy."""
    if not footprint:
        return None
    y = coord[1]
    return (y + min(footprint.keys()), y + max(footprint.keys()))


def _has_significant_visual_overlap(
    coord_a: tuple[int, int],
    footprint_a: dict[int, int],
    coord_b: tuple[int, int],
    footprint_b: dict[int, int],
    overlap_fraction: float = 0.5,
) -> bool:
    """Check whether two placed enemies visually overlap by more than overlap_fraction
    of the shorter sprite's scanline height.

    This is a separate, stricter check from the OAM budget: even if two sprites
    don't overflow the per-scanline OAM limit, having their bodies mostly
    overlapping looks wrong and wastes the formation. E.g., two Reachers
    (~69 scanlines tall) placed 16 scanlines apart still visually overlap on
    53 scanlines, which is >50% of each body.
    """
    range_a = _footprint_range(coord_a, footprint_a)
    range_b = _footprint_range(coord_b, footprint_b)
    if range_a is None or range_b is None:
        return False
    overlap_start = max(range_a[0], range_b[0])
    overlap_end = min(range_a[1], range_b[1])
    if overlap_start > overlap_end:
        return False
    overlap_scanlines = overlap_end - overlap_start + 1
    height_a = range_a[1] - range_a[0] + 1
    height_b = range_b[1] - range_b[0] + 1
    shorter = min(height_a, height_b)
    if shorter <= 0:
        return False
    return overlap_scanlines > shorter * overlap_fraction


def find_valid_coordinates(
    placed_enemies: list[tuple[tuple[int, int], dict[int, int]]],
    candidate_footprint: dict[int, int],
    valid_coordinates: list[tuple[int, int]],
    threshold: int = OAM_SCANLINE_THRESHOLD,
    overlap_fraction: float = 0.5,
) -> list[tuple[int, int]]:
    """Filter coordinates to those that pass the scanline budget check AND don't
    significantly visually overlap any already-placed enemy.

    Args:
        placed_enemies: List of ((x, y), footprint) tuples for already-placed enemies.
        candidate_footprint: The scanline footprint dict for the candidate enemy.
        valid_coordinates: List of (x, y) coordinates to evaluate.
        threshold: Max OAM entries per scanline (default 28).
        overlap_fraction: Max allowed visual overlap as a fraction of the shorter
            sprite's height (default 0.5 = 50%).

    Returns:
        List of coordinates from valid_coordinates that pass both checks. Already-
        placed coordinates are also excluded to prevent exact-coordinate overlap.
    """
    placed_coords = {c for c, _ in placed_enemies}
    result: list[tuple[int, int]] = []
    for coord in valid_coordinates:
        if coord in placed_coords:
            continue
        if not check_scanline_budget(placed_enemies, coord, candidate_footprint, threshold):
            continue
        if any(
            _has_significant_visual_overlap(
                coord, candidate_footprint, p_coord, p_fp, overlap_fraction
            )
            for p_coord, p_fp in placed_enemies
        ):
            continue
        result.append(coord)
    return result


def clear_footprint_cache() -> None:
    """Clear the module-level footprint cache."""
    _footprint_cache.clear()
