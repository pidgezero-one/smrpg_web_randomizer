"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_350.room_350_partition import partition
from randomizer.entities.rooms.room.room_350.room_350_exits import exits
from randomizer.entities.rooms.room.room_350.room_350_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E2399_ABYSS_ROOM_1_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
