"""CGRAM sprite palette rows are a scarce shared budget.

green_switch_glow.npc_palette_rows gives the layout: rows are allocated per
distinct palette_id, starting at PROTAGONIST_PALETTE_ROW + ally_sprite_buffer_size,
one row each plus extra_palette_row_count more. Sprite CGRAM ends at row 15, so a
room at ally buffer 1 has seven rows for NPC palettes.

Only the FIRST object in room order carrying a palette sets its row count --
npc_palette_rows skips later objects with `if palette in rows: continue`. Any
residency declared on a later object is silently ignored.

npc_palette_rows's dict maps palette id to each palette's *starting* row only --
it does not record how many rows past that start a palette occupies. So the
highest starting row is the highest *occupied* row only when that one palette's
own extra_palette_row_count is 0; rows_remaining has to account for it
separately. Room 166 is the deterministic (seed 1, default Settings) room where
that distinction actually bites, found by scanning all 512 rooms for one where
the highest-starting palette also has a nonzero extra.
"""
import pytest

from randomizer import main
from randomizer.logic.palette_rows import (
    EMPTY_SPRITE_ID,
    LAST_SPRITE_PALETTE_ROW,
    PROTAGONIST_PALETTE_ROW,
    npc_palette_rows,
    rows_remaining,
)
from randomizer.types.gameworld import Settings

ROOM_ID = 315
# Sunken Ship puzzle room: palette 482 (sprite 104, a spike-top statue) starts
# at row 11 and its first object carries extra_palette_row_count=3, so it
# actually occupies rows 11-14. It is also this room's highest-starting
# palette, which makes "start row" and "occupied row" diverge for the row
# that matters.
EXTRA_ROWS_ROOM_ID = 166


@pytest.fixture(scope="module")
def world():
    return main.create(1, Settings())


def _extra_for_highest_palette(world, room):
    """(highest starting row, its own extra_palette_row_count), re-derived the
    same way npc_palette_rows resolves it: from the first object, in room
    order, that carries the palette holding that row.
    """
    rows = npc_palette_rows(world, room)
    highest_row = max(rows.values())
    highest_palette = next(p for p, r in rows.items() if r == highest_row)
    for obj in room.objects:
        sprite_id = int(obj._npc.sprite_id)
        if sprite_id == EMPTY_SPRITE_ID:
            continue
        if world.get_sprite(sprite_id).palette_id != highest_palette:
            continue
        override = obj.extra_palette_row_count
        extra = obj._npc.extra_palette_row_count if override is None else override
        return highest_row, extra
    raise AssertionError("highest_palette must come from some room object")


def test_constants():
    assert PROTAGONIST_PALETTE_ROW == 8
    assert LAST_SPRITE_PALETTE_ROW == 15


def test_rows_start_after_the_ally_buffer(world):
    room = world.rooms._rooms[ROOM_ID]
    rows = npc_palette_rows(world, room)
    assert rows, "room 315 has NPC palettes"
    lowest = min(rows.values())
    assert lowest == PROTAGONIST_PALETTE_ROW + room.partition.ally_sprite_buffer_size


def test_rows_remaining_is_consistent_with_allocation(world):
    """Free rows are what remains above the highest palette's actual extent
    (start row + its own extra_palette_row_count) -- not above its start row.

    `LAST_SPRITE_PALETTE_ROW - max(rows.values())` looks right for this room
    only because every palette in room 315 has extra=0, so start row and
    occupied row coincide;
    test_rows_remaining_accounts_for_highest_palette_extra below (room 166)
    is the case that actually tells the two formulas apart.
    """
    room = world.rooms._rooms[ROOM_ID]
    highest_row, extra = _extra_for_highest_palette(world, room)
    assert rows_remaining(world, room) == LAST_SPRITE_PALETTE_ROW - highest_row - extra


def test_rows_remaining_accounts_for_highest_palette_extra(world):
    """rows_remaining must not overcount: room 166's highest-starting palette
    (row 11) has extra_palette_row_count=3, so it actually occupies rows
    11-14 and only row 15 is free -- one row, not the four rows that
    LAST_SPRITE_PALETTE_ROW - max(rows.values()) would report.
    """
    room = world.rooms._rooms[EXTRA_ROWS_ROOM_ID]
    highest_row, extra = _extra_for_highest_palette(world, room)
    assert extra > 0, "fixture room no longer exercises extra>0; pick a new one"

    correct = LAST_SPRITE_PALETTE_ROW - highest_row - extra
    naive = LAST_SPRITE_PALETTE_ROW - highest_row
    assert correct < naive, "sanity check that this room exercises the overcount"
    assert rows_remaining(world, room) == correct


def test_green_switch_glow_still_imports_it(world):
    """The glow feature must keep working through the moved function."""
    from randomizer.logic import green_switch_glow

    assert green_switch_glow.npc_palette_rows is npc_palette_rows
