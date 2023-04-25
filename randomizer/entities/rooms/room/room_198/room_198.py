"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_198.room_198_partition import partition
from randomizer.entities.rooms.room.room_198.room_198_exits import exits
from randomizer.entities.rooms.room.room_198.room_198_objects import objects

room = Room(
    partition=partition,
    music=M32_AND_MY_NAMES_BOOSTER,
    entrance_event=E2805_TOWER_APPRENTICE_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
