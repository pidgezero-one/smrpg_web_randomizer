"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_196.room_196_partition import partition
from randomizer.entities.rooms.room.room_196.room_196_exits import exits
from randomizer.entities.rooms.room.room_196.room_196_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E2335_TOWER_FIRST_STAIRCASE_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
