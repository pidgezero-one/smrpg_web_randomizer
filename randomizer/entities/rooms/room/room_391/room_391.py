"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_391.room_391_partition import partition
from randomizer.entities.rooms.room.room_391.room_391_exits import exits
from randomizer.entities.rooms.room.room_391.room_391_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3341_VOLCANO_SMALL_BOSS_PATH_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
