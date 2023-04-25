"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_247.room_247_partition import partition

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1521_CLONE_RESERVED,
    events=[],
    exits=[],
    objects=[],
    extra_sprite_actions=[],
)
