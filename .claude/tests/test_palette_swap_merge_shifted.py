"""Offset-shifted merges need residency AND application.

extra_palette_source_offset / extra_palette_row_count make the palette rows
available in the level; A_IncPaletteRowBy moves the object onto one and requires
residency to already be set. Same pairing as room 422, where SHARED_ITEM_BASE
loads the rows and A_IncPaletteRowBy(2) recolours the frog coins.

Residency goes on the object BEING RECOLOURED, not on the first object carrying
that palette -- confirmed in-game via the pink Yoshi NPC, which uses
source_offset=1, row_count=1 for a +1 shift. The generator selects canonical by
(palette_offset, sprite_id), so the canonical is always the class's lowest
offset and every merge delta is >= 0 -- a canonical-sprite object never needs a
bump or residency of its own.
"""
import copy
import inspect

import pytest

from randomizer import main
from randomizer.data.sprites.palette_swap_classes import SHIFTED
from randomizer.logic.partition_calculator import _MAX_PACK_SPAN, _merge_palette_swaps
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


def test_residency_lands_on_the_recoloured_object(world, room):
    """Residency (extra_palette_source_offset / extra_palette_row_count) goes on
    the object BEING RECOLOURED, not on whichever object happens to carry the
    palette first. Confirmed in-game via the pink Yoshi NPC, which sets
    source_offset=1 / row_count=1 for a +1 shift. Object 0 (BANDANA_RED) is the
    canonical here and already renders at its own native palette_offset, so it
    needs no residency at all -- its fields must stay untouched (None)."""
    canonical, shifted_offset = SHIFTED[BANDANA_BLUE]
    assert canonical == BANDANA_RED
    canonical_offset = world.get_sprite(BANDANA_RED).palette_offset
    delta = shifted_offset - canonical_offset
    assert delta > 0, "test assumes BANDANA_BLUE sits above BANDANA_RED's offset"

    room.objects[0]._npc = _record_with_sprite(room.objects[0]._npc, BANDANA_RED)
    room.objects[1]._npc = _record_with_sprite(room.objects[1]._npc, BANDANA_BLUE)

    _merge_palette_swaps(world, ROOM_ID)

    assert room.objects[1].extra_palette_source_offset == delta
    assert room.objects[1].extra_palette_row_count == delta
    assert room.objects[0].extra_palette_source_offset is None
    assert room.objects[0].extra_palette_row_count is None


def test_canonical_offset_is_always_the_class_minimum(world):
    """The generator selects canonical by (palette_offset, sprite_id), not by
    sprite id alone -- palette_offset lives on the SPRITE, and an object merged
    onto the canonical inherits it as a rendering baseline that
    A_IncPaletteRowBy can only increase. So the canonical must be the class
    member with the lowest palette_offset, or some other member would need a
    negative bump to reach it.

    This is the invariant that makes every delta in _merge_palette_swaps'
    participants loop non-negative, which is in turn why a canonical object
    never needs a bump. Pin it directly against the checked-in table instead of
    one example: prior to the generator fix, 23 of the 156 current SHIFTED
    classes had a canonical whose own offset sat ABOVE another member's
    (e.g. Valentina's Birdy/Bluebird, spr148 at offset 3 vs member spr269 at 0).
    """
    for source, (canonical, offset) in SHIFTED.items():
        canonical_offset = world.get_sprite(canonical).palette_offset
        assert canonical_offset <= offset, (
            f"sprite {canonical} (canonical for source {source}) has "
            f"palette_offset {canonical_offset}, which is above member "
            f"{source}'s offset {offset} -- A_IncPaletteRowBy cannot express "
            f"the resulting negative bump"
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
    """extra_palette_row_count is a 2-bit field (max 3), so a class whose delta
    from its canonical exceeds that cannot get residency at all.

    Per the 2026-07-30 "never skip a merge" ruling this must NOT skip the
    sprite_id merge -- only the residency declaration (and its bump) are
    skipped, with a log line; the object then renders in the canonical palette
    instead of its own. Saving the clone buffer is the point; a wrong palette
    row is a cosmetic degradation vanilla itself ships (rooms 5 and 7 coexist
    two palette offsets with extra_palette_row_count=0).

    Unlike a truncated-but-still-declared value, the source does a full skip:
    `declared = min(delta, _MAX_PACK_SPAN, free)`; when `declared < delta` it
    logs and `continue`s *before* calling set_extra_palette_source_offset /
    set_extra_palette_row_count or appending to bumps. So the recoloured
    object's residency fields stay None and it gets no bumps entry -- verified
    against _merge_palette_swaps' source directly (not re-derived here).

    delta is computed against the canonical's own offset (not the source's raw
    table offset) so the ">" test is correct even for a class whose canonical
    doesn't sit at 0 -- see test_canonical_offset_is_always_the_class_minimum,
    which only pins canonical_offset <= offset, not canonical_offset == 0.
    """
    wide = [
        source for source, (canonical, offset) in SHIFTED.items()
        if offset - world.get_sprite(canonical).palette_offset > _MAX_PACK_SPAN
    ]
    if not wide:
        pytest.skip("no class in the table spans more than _MAX_PACK_SPAN pack rows")
    source = wide[0]
    canonical, offset = SHIFTED[source]

    room.objects[0]._npc = _record_with_sprite(room.objects[0]._npc, canonical)
    room.objects[1]._npc = _record_with_sprite(room.objects[1]._npc, source)

    bumps = _merge_palette_swaps(world, ROOM_ID)

    assert _sprite_of(room.objects[1]) == canonical, (
        "the merge must happen even when residency can't fully cover the span"
    )
    assert room.objects[1].extra_palette_source_offset is None, (
        "declared < delta must skip residency entirely, not truncate it"
    )
    assert room.objects[1].extra_palette_row_count is None, (
        "declared < delta must skip residency entirely, not truncate it"
    )
    assert not any(index == 1 for index, _ in bumps), (
        f"object 1 must not get a bump when residency can't be declared, got {bumps}"
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
