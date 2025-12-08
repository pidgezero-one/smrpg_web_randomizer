"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_510.room_510_partition import partition

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0079_UNKNOWN,
    events=[],
    exits=[],
    objects=[],
    extra_sprite_actions=[])
