"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_199.room_199_partition import partition
from randomizer.entities.rooms.room.room_199.room_199_exits import exits
from randomizer.entities.rooms.room.room_199.room_199_objects import objects

room = Room(
    partition=partition,
    music=M32_AND_MY_NAMES_BOOSTER,
    entrance_event=E2364_TOWER_TOP_FLOOR_CHEST_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
