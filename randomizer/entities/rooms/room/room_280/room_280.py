"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_280.room_280_partition import partition
from randomizer.entities.rooms.room.room_280.room_280_exits import exits
from randomizer.entities.rooms.room.room_280.room_280_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
