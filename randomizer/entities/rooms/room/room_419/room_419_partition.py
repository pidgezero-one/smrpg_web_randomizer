"""Partition import"""

from randomizer.entities.rooms.partition_imports import *

buffers: list[Buffer] = [
    Buffer(
        buffer_type=BufferType.TREASURE_CHEST,
        main_buffer_space=BufferSpace.BYTES_0,
        index_in_main_buffer=True),
    Buffer(
        buffer_type=BufferType.EMPTY_3,
        main_buffer_space=BufferSpace.BYTES_0,
        index_in_main_buffer=True),
    Buffer(
        buffer_type=BufferType.COINS,
        main_buffer_space=BufferSpace.BYTES_0,
        index_in_main_buffer=True),
]

partition = Partition(
    ally_sprite_buffer_size=1,
    allow_extra_sprite_buffer=False,
    extra_sprite_buffer_size=0,
    buffers=buffers,
    full_palette_buffer=True)
