"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_260.room_260_partition import partition

room = Room(
    partition=partition,
    music=M30_LONG_LONG_AGO,
    entrance_event=E1718_EMPTY,
    events=[],
    exits=[],
    objects=[],
    extra_sprite_actions=[],
)
