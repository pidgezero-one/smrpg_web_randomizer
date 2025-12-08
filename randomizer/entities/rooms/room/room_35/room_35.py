"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_35.room_35_partition import partition
from randomizer.entities.rooms.room.room_35.room_35_exits import exits
from randomizer.entities.rooms.room.room_35.room_35_objects import objects

room = Room(
    partition=partition,
    music=M32_AND_MY_NAMES_BOOSTER,
    entrance_event=E2315_TOWER_PARACHUTE_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
