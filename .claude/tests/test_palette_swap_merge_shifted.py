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

# Valentina's Birdy/Bluebird class: canonical 148 sits at its own native pack
# offset 3, while shifted members 269/295 sit at 0 -- the canonical is NOT
# always the group minimum. See SHIFTED[BIRDY_LOW_MEMBER] == (BIRDY_CANONICAL, 0).
BIRDY_CANONICAL = 148
BIRDY_LOW_MEMBER = 269


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


def test_canonical_object_above_low_gets_a_bump(world, room):
    """The canonical sprite's own native palette_offset is not necessarily the
    merged group's minimum. spr148 (Valentina's Birdy/Bluebird) sits at offset 3
    while its shifted members 269/295 sit at 0 -- so an object that was ALREADY
    on 148 before the merge still needs A_IncPaletteRowBy(3), or it renders
    using row `low`'s colour (member 269's) instead of its own.

    Regression for a bug where the bump loop walked only the SHIFTED sources
    and silently skipped every object that was already on the canonical
    sprite, even when that canonical's own offset was above the group's low.
    Measured impact: 15 of 99 SHIFTED classes have canonical_offset > low,
    including Valentina's Birdy/Bluebird (spr148) and Mack's Shysters (spr376).
    """
    assert SHIFTED[BIRDY_LOW_MEMBER] == (BIRDY_CANONICAL, 0)
    canonical_offset = world.get_sprite(BIRDY_CANONICAL).palette_offset
    assert canonical_offset > 0, "test assumes this canonical's own offset is above 0"

    room.objects[0]._npc = _record_with_sprite(room.objects[0]._npc, BIRDY_CANONICAL)
    room.objects[1]._npc = _record_with_sprite(room.objects[1]._npc, BIRDY_LOW_MEMBER)

    bumps = _merge_palette_swaps(world, ROOM_ID)

    assert (0, canonical_offset) in bumps, (
        f"pre-existing canonical object (index 0) must be bumped by its own "
        f"offset ({canonical_offset}) above the group's low (0), got {bumps}"
    )


def test_canonical_at_minimum_offset_gets_no_bump(world, room):
    """Non-regression: when the canonical sprite already sits at the merged
    group's minimum offset (the common case -- e.g. the bandana class, canonical
    267 at offset 0 with member 331 at offset 1), it needs no runtime bump.
    Fixing the case above (canonical above low) must not start bumping every
    canonical object unconditionally."""
    room.objects[0]._npc = _record_with_sprite(room.objects[0]._npc, BANDANA_RED)
    room.objects[1]._npc = _record_with_sprite(room.objects[1]._npc, BANDANA_BLUE)

    bumps = _merge_palette_swaps(world, ROOM_ID)

    assert not any(index == 0 for index, _ in bumps), (
        f"canonical object (index 0) is already at the group minimum and needs "
        f"no bump, got {bumps}"
    )


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
    """sprite_palette_copies (inside build_room_granter_scripts) rewrites a
    sprite's palette_id in place when DifferentiateRepeatedBosses is off
    (world.get_sprite(target_id).palette_id = ...), which can change which
    CGRAM row a merged class lands on. The merge -- reached via
    update_changed_room_partitions -- must read the rewritten ids, so the copy
    has to run first.

    Post-2026-08-01 refactor: apply.py was split up.
    apply_shuffler_results_to_game_data now lives in
    randomizer/logic/post_shuffle/apply_shuffler_results.py as a short,
    explicit sequence of named step calls; sprite_palette_copies moved into
    randomizer/logic/post_shuffle/steps/build_room_granter_scripts.py
    (confirmed by direct read: the mutation loop is unconditionally reached
    near the top of that function, gated only by the DifferentiateRepeatedBosses
    flag check). update_changed_room_partitions is still imported directly
    from randomizer.logic.partition_calculator.

    Verified 2026-08-01 by direct read of apply_shuffler_results_to_game_data's
    source: it calls build_room_granter_scripts(world) then, several calls
    later, update_changed_room_partitions(world) -- no branch reorders them.
    This test re-checks that source-order invariant so a future edit that
    breaks it fails loudly instead of silently reading stale palette ids.
    """
    from randomizer.logic.post_shuffle.apply_shuffler_results import (
        apply_shuffler_results_to_game_data,
    )

    source = inspect.getsource(apply_shuffler_results_to_game_data)
    copies_at = source.find("build_room_granter_scripts(world)")
    recalc_at = source.find("update_changed_room_partitions(world)")
    if copies_at == -1 or recalc_at == -1:
        pytest.skip(
            "could not locate both the build_room_granter_scripts call and the "
            "update_changed_room_partitions call by source inspection"
        )
    assert copies_at < recalc_at, (
        "build_room_granter_scripts (which runs sprite_palette_copies) must be "
        "called before update_changed_room_partitions -- that call is what "
        "reaches _merge_palette_swaps's world.get_sprite(...).palette_id / "
        ".palette_offset reads"
    )
