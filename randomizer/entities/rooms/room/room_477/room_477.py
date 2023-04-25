"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_477.room_477_partition import partition
from randomizer.entities.rooms.room.room_477.room_477_exits import exits
from randomizer.entities.rooms.room.room_477.room_477_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E2144_KEEP_2ND_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
