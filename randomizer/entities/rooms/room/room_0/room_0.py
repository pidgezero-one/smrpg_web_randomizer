"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_0.room_0_partition import partition

room = Room(
    partition=partition,
    music=M02_MUSHROOM_KINGDOM,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=[],
    exits=[],
    objects=[],
    extra_sprite_actions=[])
