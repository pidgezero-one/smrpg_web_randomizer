"""CGRAM sprite palette row layout - a scarce shared budget.

Overworld CGRAM layout: row 0 is untouched by event scripts, rows 1-7 are
background palettes, row 8 is the protagonist, rows 9-15 are NPCs.
ally_sprite_buffer_size > 1 extends the protagonist across rows
8..8+size-1 and NPC rows start after it.

NPC rows are handed out **per distinct palette id, in object order** - not
per sprite. Two sprites sharing a palette share one row, and an NPC whose
palette id matches the protagonist's gets no row at all because the
protagonist's row already covers it.

npc_palette_rows, protagonist_palette_id and PROTAGONIST_PALETTE_ROW
moved here verbatim from green_switch_glow.py, which re-imports them so its
existing callers are unaffected. This was a general room-layout primitive
that happened to live in a single feature module; the palette-swap merge
pass is a second consumer, via rows_remaining below.
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from ..utils.npcs import PROTAGONIST_BASE_SPRITE_ID

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld
    from randomizer.types.room import Room


PROTAGONIST_PALETTE_ROW = 8
EMPTY_SPRITE_ID = 1023  # draws nothing and takes no palette row (see room 227)

# Sprite palettes occupy CGRAM rows 8-15. Row 8 is the protagonist's; each
# ally_sprite_buffer_size unit pushes the first NPC palette up by one.
LAST_SPRITE_PALETTE_ROW = 15


def protagonist_palette_id(world: GameWorld) -> int | None:
    """The palette id the protagonist's row holds, or None if it can't be resolved."""
    ally_index = world.overworld_character.ally.index
    if ally_index not in PROTAGONIST_BASE_SPRITE_ID:
        return None
    return world.get_sprite(PROTAGONIST_BASE_SPRITE_ID[ally_index]).palette_id


def npc_palette_rows(world: GameWorld, room: Room) -> dict[int, int]:
    """CGRAM row each distinct NPC palette id occupies in room."""
    partition = room.partition
    assert partition is not None, "room has no partition"

    protagonist_palette = protagonist_palette_id(world)
    rows: dict[int, int] = {}
    row = PROTAGONIST_PALETTE_ROW + partition.ally_sprite_buffer_size
    for obj in room.objects:
        sprite_id = int(obj._npc.sprite_id)
        if sprite_id == EMPTY_SPRITE_ID:
            continue
        palette = world.get_sprite(sprite_id).palette_id
        if palette == protagonist_palette or palette in rows:
            # Already resident - the protagonist's row, or a row this palette
            # was given by an earlier object.
            continue
        override = obj.extra_palette_row_count
        extra = obj._npc.extra_palette_row_count if override is None else override
        rows[palette] = row
        row += 1 + extra
    return rows


def rows_remaining(world: GameWorld, room: Room) -> int:
    """Free CGRAM sprite palette rows in room after current allocations.

    npc_palette_rows records each palette's *starting* row, not the rows it
    occupies - a palette claiming extra_palette_row_count more rows spans
    that many rows past its start (see reference_effects_npc_palette_row:
    some effects records target hardcoded rows, so growing residency is
    never free). The highest start row equals the highest *occupied* row
    only when that one palette's own extra is 0; otherwise treating them as
    the same overcounts the free rows by exactly that extra, which could let
    a caller approve a merge that actually overflows CGRAM. For example,
    room 166 has a palette starting at row 11 with extra=3 (occupying rows
    11-14): the naive LAST_SPRITE_PALETTE_ROW - 11 claims 4 free rows, but
    only row 15 (1 row) is actually free.

    The returned dict does not carry extras (see its docstring), so the
    highest-row palette's own extra is re-resolved here the same way
    npc_palette_rows resolves it: from the first room object, in room
    order, that carries that palette.
    """
    rows = npc_palette_rows(world, room)
    if not rows:
        partition = room.partition
        assert partition is not None, "room has no partition"
        first_row = PROTAGONIST_PALETTE_ROW + partition.ally_sprite_buffer_size
        return LAST_SPRITE_PALETTE_ROW - first_row + 1

    highest_row = max(rows.values())
    highest_palette = next(
        palette for palette, row in rows.items() if row == highest_row
    )

    extra = None
    for obj in room.objects:
        sprite_id = int(obj._npc.sprite_id)
        if sprite_id == EMPTY_SPRITE_ID:
            continue
        if world.get_sprite(sprite_id).palette_id != highest_palette:
            continue
        override = obj.extra_palette_row_count
        extra = obj._npc.extra_palette_row_count if override is None else override
        break
    assert extra is not None, (
        "highest_palette came from npc_palette_rows, so some object must carry it"
    )

    return LAST_SPRITE_PALETTE_ROW - highest_row - extra
