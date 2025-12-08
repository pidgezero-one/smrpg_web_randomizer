"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_19.room_19_partition import partition
from randomizer.entities.rooms.room.room_19.room_19_exits import exits

room = Room(
    partition=partition,
    music=M02_MUSHROOM_KINGDOM,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=[],
    extra_sprite_actions=[])
