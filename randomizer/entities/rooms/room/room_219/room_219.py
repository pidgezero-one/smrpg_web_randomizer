"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_219.room_219_partition import partition

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=[],
    exits=[],
    objects=[],
    extra_sprite_actions=[])
