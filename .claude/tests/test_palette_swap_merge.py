"""Merging palette-swap-equivalent sprites frees clone buffers.

A buffer holds exactly one sprite_id, and a room has three. Sprites that are
byte-identical apart from palette_offset can share one buffer once they share a
sprite_id, which is what this pass arranges. It runs before Step 3 of
_recalculate_room_partition, because Step 3 is where "one buffer per unique
sprite ID" is decided.
"""
import copy

import pytest

from randomizer import main
from randomizer.data.sprites.palette_swap_classes import PURE
from randomizer.logic.partition_calculator import (
    _merge_palette_swaps,
    _recalculate_room_partition,
)
from randomizer.types.gameworld import Settings

ROOM_ID = 315


@pytest.fixture(scope="module")
def world():
    return main.create(1, Settings())


def _sprite_of(obj):
    """A room object's effective sprite is its NPC record's sprite_id.

    Room objects have no per-object sprite override: `RegularNPC` exposes no
    `sprite_id` attribute at all, `BaseRoomObject._sprite_id` is written by
    `set_sprite_id` and read by nothing, and both `_get_npc_signature` and
    `_render_npc` key on the record. Merging therefore swaps the record.
    """
    return int(obj._npc.sprite_id)


@pytest.fixture
def restore_npcs(world):
    """Restore every object's NPC record. Records are shared across rooms, so a
    leaked mutation corrupts unrelated rooms -- see the room 41 landmine."""
    room = world.rooms._rooms[ROOM_ID]
    saved = [obj._npc for obj in room.objects]
    yield room
    for obj, npc in zip(room.objects, saved):
        obj._npc = npc


def _record_with_sprite(npc, sprite_id):
    """A copy of `npc` pointing at `sprite_id`, leaving the shared original alone."""
    record = copy.copy(npc)
    record.set_sprite_id(sprite_id)
    return record


def test_pure_duplicate_is_rewritten_to_canonical(world, restore_npcs):
    """An object whose record carries a PURE source sprite ends up on the canonical."""
    room = restore_npcs
    source, canonical = next(iter(PURE.items()))

    obj = room.objects[0]
    obj._npc = _record_with_sprite(obj._npc, source)

    _merge_palette_swaps(world, ROOM_ID)

    assert _sprite_of(obj) == canonical


def test_pure_merge_emits_no_row_bumps(world, restore_npcs):
    """Pure duplicates share palette_offset, so nothing needs A_IncPaletteRowBy."""
    room = restore_npcs
    source, _ = next(iter(PURE.items()))

    obj = room.objects[0]
    obj._npc = _record_with_sprite(obj._npc, source)

    assert _merge_palette_swaps(world, ROOM_ID) == []


def test_merge_does_not_mutate_the_shared_record(world, restore_npcs):
    """The pass must copy, never mutate in place -- NPC records are global."""
    room = restore_npcs
    source, canonical = next(iter(PURE.items()))

    obj = room.objects[0]
    shared = _record_with_sprite(obj._npc, source)
    obj._npc = shared

    _merge_palette_swaps(world, ROOM_ID)

    assert int(shared.sprite_id) == source, "the pass mutated the record in place"
    assert obj._npc is not shared


def test_merge_reduces_distinct_sprite_count(world, restore_npcs):
    """Two objects on the two halves of a PURE class collapse to one sprite."""
    room = restore_npcs
    source, canonical = next(iter(PURE.items()))

    obj_a, obj_b = room.objects[0], room.objects[1]
    obj_a._npc = _record_with_sprite(obj_a._npc, canonical)
    obj_b._npc = _record_with_sprite(obj_b._npc, source)

    _merge_palette_swaps(world, ROOM_ID)

    assert _sprite_of(obj_a) == _sprite_of(obj_b) == canonical


def test_merge_is_idempotent(world, restore_npcs):
    """Running twice must not change anything the second time."""
    room = restore_npcs
    source, canonical = next(iter(PURE.items()))

    obj = room.objects[0]
    obj._npc = _record_with_sprite(obj._npc, source)

    _merge_palette_swaps(world, ROOM_ID)
    first = _sprite_of(obj)
    assert _merge_palette_swaps(world, ROOM_ID) == []
    assert _sprite_of(obj) == first == canonical


def test_recalculate_still_succeeds_with_merge_in_place(world):
    """The pass runs inside _recalculate_room_partition without breaking it."""
    _recalculate_room_partition(world, ROOM_ID)
    room = world.rooms._rooms[ROOM_ID]
    assert room.partition is not None
    assert len(room.partition.buffers) == 3
