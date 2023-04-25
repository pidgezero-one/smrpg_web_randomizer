"""Partition import"""

from typing import List

from randomizer.entities.rooms.partition_imports import *

buffers: List[Buffer] = [
    Buffer(
        buffer_type=BufferType.EMPTY_3,
        main_buffer_space=BufferSpace.BYTES_0,
        index_in_main_buffer=True,
    ),
    Buffer(
        buffer_type=BufferType.THREE_SPRITES_PER_ROW,
        main_buffer_space=BufferSpace.BYTES_0,
        index_in_main_buffer=True,
    ),
    Buffer(
        buffer_type=BufferType.THREE_SPRITES_PER_ROW,
        main_buffer_space=BufferSpace.BYTES_0,
        index_in_main_buffer=True,
    ),
]

partition = Partition(
    ally_sprite_buffer_size=1,
    allow_extra_sprite_buffer=True,
    extra_sprite_buffer_size=1,
    buffers=buffers,
    full_palette_buffer=True,
)
