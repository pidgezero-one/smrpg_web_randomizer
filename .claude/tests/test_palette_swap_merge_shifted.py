"""Offset-shifted merges need residency AND application.

extra_palette_source_offset / extra_palette_row_count make the palette rows
available in the level; A_IncPaletteRowBy moves the object onto one and requires
residency to already be set. Same pairing as room 422, where SHARED_ITEM_BASE
loads the rows and A_IncPaletteRowBy(2) recolours the frog coins.

Residency goes on the FIRST object in room order carrying that palette_id --
npc_palette_rows skips later objects with `if palette in rows: continue`, so
residency declared on a later merged object is silently ignored.
"""
import copy
import inspect

import pytest

from randomizer import main
from randomizer.data.sprites.palette_swap_classes import SHIFTED
from randomizer.logic.partition_calculator import _merge_palette_swaps
from randomizer.types.gameworld import Settings

ROOM_ID = 315
BANDANA_BLUE = 331
BANDANA_RED = 267


@pytest.fixture(scope="module")
def world():
    return main.create(1, Settings())


def _sprite_of(obj):
    return int(obj._npc.sprite_id)


def _record_with_sprite(npc, sprite_id):
    """A copy of `npc` pointing at `sprite_id`, leaving the shared original alone."""
    record = copy.copy(npc)
    record.set_sprite_id(sprite_id)
    return record


@pytest.fixture
def room(world):
    """Restore every object override this module touches."""
    r = world.rooms._rooms[ROOM_ID]
    saved = [
        (o._npc, o.extra_palette_source_offset, o.extra_palette_row_count)
        for o in r.objects
    ]
    yield r
    for obj, (npc, source, count) in zip(r.objects, saved):
        obj._npc = npc
        obj.set_extra_palette_source_offset(source)
        obj.set_extra_palette_row_count(count)


def test_shifted_source_is_rewritten_to_canonical(world, room):
    room.objects[0]._npc = _record_with_sprite(room.objects[0]._npc, BANDANA_RED)
    room.objects[1]._npc = _record_with_sprite(room.objects[1]._npc, BANDANA_BLUE)

    _merge_palette_swaps(world, ROOM_ID)

    assert _sprite_of(room.objects[1]) == BANDANA_RED


def test_shifted_merge_returns_a_bump_for_the_shifted_object(world, room):
    room.objects[0]._npc = _record_with_sprite(room.objects[0]._npc, BANDANA_RED)
    room.objects[1]._npc = _record_with_sprite(room.objects[1]._npc, BANDANA_BLUE)

    bumps = _merge_palette_swaps(world, ROOM_ID)

    assert (1, 1) in bumps, f"expected object 1 to need a +1 row bump, got {bumps}"
    assert not any(index == 0 for index, _ in bumps), "object 0 is already canonical"


def test_residency_lands_on_the_first_object_with_that_palette(world, room):
    """Object 0 carries the palette first, so the row count belongs to it --
    declaring it on object 1 would be silently ignored by npc_palette_rows."""
    room.objects[0]._npc = _record_with_sprite(room.objects[0]._npc, BANDANA_RED)
    room.objects[1]._npc = _record_with_sprite(room.objects[1]._npc, BANDANA_BLUE)

    _merge_palette_swaps(world, ROOM_ID)

    assert room.objects[0].extra_palette_row_count == 1
    assert room.objects[0].extra_palette_source_offset == 0


def test_merge_never_skipped_when_span_exceeds_residency_field(world, room):
    """extra_palette_row_count is a 2-bit field (max 3), so a class whose source
    sits more than 3 pack rows from its canonical cannot get full residency.

    Per the 2026-07-30 "never skip a merge" ruling this must NOT skip the
    sprite_id merge -- only the residency declaration is truncated (with a log
    line), and rows beyond the truncated span render in the canonical palette
    instead of their own. Saving the clone buffer is the point; a wrong
    palette row is a cosmetic degradation vanilla itself ships (rooms 5 and 7
    coexist two palette offsets with extra_palette_row_count=0).

    declared <= 3 is a structural invariant of the field itself (the setter
    asserts it). declared < offset is guaranteed by declared <= 3 < offset
    (the `wide` filter), independent of the room's free-row budget or of
    where the canonical's own native pack offset falls -- so this holds
    whether the field cap or the CGRAM row budget is what actually binds.
    """
    wide = [s for s, (_, off) in SHIFTED.items() if off > 3]
    if not wide:
        pytest.skip("no class in the table spans more than 3 pack rows")
    source = wide[0]
    canonical, offset = SHIFTED[source]

    room.objects[0]._npc = _record_with_sprite(room.objects[0]._npc, canonical)
    room.objects[1]._npc = _record_with_sprite(room.objects[1]._npc, source)

    _merge_palette_swaps(world, ROOM_ID)

    assert _sprite_of(room.objects[1]) == canonical, (
        "the merge must happen even when residency can't fully cover the span"
    )
    declared = room.objects[0].extra_palette_row_count
    assert 0 <= declared <= 3, "extra_palette_row_count is a 2-bit field (max 3)"
    assert declared < offset, (
        f"residency (extra_palette_row_count={declared}) should be truncated, "
        f"not cover the full {offset}-row pack offset -- the 2-bit field caps "
        "at 3 and this class was chosen to exceed that"
    )


def test_no_bump_when_room_has_no_stub(world, room):
    """Tier 2 needs an injection point. Without one the merge is skipped, but
    tier 1 still applies."""
    from randomizer.data.rooms.sprite_loader_events import ROOM_SPRITE_LOADER

    unstubbed = [
        rid
        for rid, r in enumerate(world.rooms._rooms)
        if r is not None and rid not in ROOM_SPRITE_LOADER and len(r.objects) >= 2
    ]
    if not unstubbed:
        pytest.skip("every room with objects has a stub")
    target = unstubbed[0]
    other = world.rooms._rooms[target]
    saved = [o._npc for o in other.objects]
    try:
        other.objects[0]._npc = _record_with_sprite(other.objects[0]._npc, BANDANA_RED)
        other.objects[1]._npc = _record_with_sprite(other.objects[1]._npc, BANDANA_BLUE)
        bumps = _merge_palette_swaps(world, target)
        assert bumps == []
    finally:
        for obj, npc in zip(other.objects, saved):
            obj._npc = npc


def test_merge_reads_post_copy_palette_ids():
    """apply.py's sprite_palette_copies rewrites a sprite's palette_id in place
    when DifferentiateRepeatedBosses is off (world.get_sprite(target_id).palette_id
    = ...), which can change which CGRAM row a merged class lands on. The merge --
    reached from apply_shuffler_results_to_game_data via
    update_changed_room_partitions -- must read the rewritten ids, so the copy has
    to run first in source order.

    Verified 2026-07-30 by direct line inspection of apply.py: the
    sprite_palette_copies block (~line 507) runs strictly before the
    update_changed_room_partitions(world) call (~line 1126), both inside
    apply_shuffler_results_to_game_data, with no branch that reorders them.
    This test re-checks that source-order invariant so a future edit that
    breaks it fails loudly instead of silently reading stale palette ids.
    """
    from randomizer.logic.apply import apply_shuffler_results_to_game_data

    source = inspect.getsource(apply_shuffler_results_to_game_data)
    copies_at = source.find("sprite_palette_copies")
    recalc_at = source.find("update_changed_room_partitions(world)")
    if copies_at == -1 or recalc_at == -1:
        pytest.skip(
            "could not locate both sprite_palette_copies and the "
            "update_changed_room_partitions(world) call by source inspection"
        )
    assert copies_at < recalc_at, (
        "sprite_palette_copies must run before update_changed_room_partitions "
        "-- that call is what reaches _merge_palette_swaps's "
        "world.get_sprite(...).palette_id / .palette_offset reads"
    )
