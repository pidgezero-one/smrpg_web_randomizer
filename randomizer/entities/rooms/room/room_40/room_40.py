"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_40.room_40_partition import partition
from randomizer.entities.rooms.room.room_40.room_40_exits import exits
from randomizer.entities.rooms.room.room_40.room_40_objects import objects

room = Room(
    partition=partition,
    music=M32_AND_MY_NAMES_BOOSTER,
    entrance_event=E2417_TOWER_CHOMP_STAIRWAY_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
