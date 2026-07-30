"""Dedicated NPC VRAM must never reach clone buffer A.

Clone buffer bases are literals in the engine -- $C0:8E98-$C0:8EB7 loads #$40,
#$80, #$C0 for buffers A, B and C -- and $C0:8F83 writes that base into the same
object field ($18,X) the dedicated path fills from the packed cursor $6D. So
dedicated NPCs own packed $00-$3F and nothing more. The only guard
($C0:8ED4-$C0:8EFD) stops a block straddling packed $20 or $30; both sit below
$40. A cursor that walks past $40 silently allocates on top of buffer A.
"""
import pytest

from randomizer import main
from randomizer.logic.partition_calculator import _recalculate_room_partition
from randomizer.types.gameworld import Settings
from smrpgpatchbuilder.datatypes.levels.classes import BufferType

ROOM_ID = 315

# $C0:8E9B loads #$40 as clone buffer A's base, in the same packed units as $6D.
PACKED_BUFFER_A = 0x40


def linear(packed: int) -> int:
    """Packed cursor is (row << 4) | col with 8 columns per row ($C0:B830)."""
    return (packed >> 4) * 8 + (packed & 0x0F)


def packed_add(packed: int, slots: int) -> int:
    """$C0:B830: add slots to a packed cursor, carrying columns into rows."""
    col = (packed & 0x0F) + slots
    return (packed & 0xF0) + ((col & 0xF8) << 1) + (col & 0x07)


def dedicated_high_water(world, room_id: int) -> int:
    """Replay $C0:8FF9 cursor init + $C0:8EBC allocation, return the end cursor.

    Mirrors the engine exactly: ally buffer, then the extra sprite buffer only if
    allowed, then each buffer's main_buffer_space, then one block of
    4 * (min_vram_size + 1) slots per cannot_clone NPC in room-object order, with
    the straddle realign at $C0:8ED4.
    """
    room = world.rooms._rooms[room_id]
    partition = room.partition
    assert partition is not None

    cursor = partition.ally_sprite_buffer_size * 4
    if partition.allow_extra_sprite_buffer:
        cursor += (partition.extra_sprite_buffer_size + 1) * 4
    for buf in partition.buffers:
        cursor += buf.main_buffer_space * 4

    # $C0:908E-$C0:90AA: $01D5 is $41 when buffer A is not EMPTY_3, else $61,
    # selecting the $20 or $30 straddle boundary.
    boundary = 0x20 if partition.buffers[0].buffer_type != BufferType.EMPTY_3 else 0x30

    for obj in room.objects:
        cc = obj.cannot_clone
        if cc is None:
            cc = obj._npc.cannot_clone
        if not cc:
            continue
        mv = obj.min_vram_size
        if mv is None:
            mv = obj._npc.min_vram_size
        slots = 4 * (mv + 1)
        base = cursor
        end = packed_add(base, slots)
        # $C0:8ED0: min_vram_size == 0 skips the straddle check completely.
        if mv != 0 and end > boundary and base < boundary:
            base = boundary
            end = packed_add(base, slots)
        cursor = end
    return cursor


@pytest.fixture(scope="module")
def world():
    return main.create(1, Settings())


def test_object_8_is_not_force_dedicated(world):
    """The room-level cannot_clone override on object 8 is a Yaridovich-era
    hardcode. It must be absent so Step 7 can auto-decide -- sharing buffer C
    when the slot's sprite is already buffered, and sizing min_vram_size
    correctly when it is not."""
    room = world.rooms._rooms[ROOM_ID]
    assert room.objects[8].cannot_clone is None


def test_dedicated_allocations_stay_below_buffer_a(world):
    """With object 8's cannot_clone override removed, the cursor must end below
    packed $40. It reached exactly $40 before, putting object 8's block on top
    of object 0."""
    _recalculate_room_partition(world, ROOM_ID)

    high_water = dedicated_high_water(world, ROOM_ID)
    assert linear(high_water) < linear(PACKED_BUFFER_A), (
        f"dedicated cursor reached packed ${high_water:02X} "
        f"(linear {linear(high_water)}); buffer A starts at linear "
        f"{linear(PACKED_BUFFER_A)}"
    )
