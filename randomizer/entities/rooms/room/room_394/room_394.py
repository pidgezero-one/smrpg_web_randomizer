"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_394.room_394_partition import partition
from randomizer.entities.rooms.room.room_394.room_394_exits import exits
from randomizer.entities.rooms.room.room_394.room_394_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3342_VOLCANO_5TH_BOSS_PATH_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
