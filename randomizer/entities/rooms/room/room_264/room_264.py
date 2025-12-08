"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_264.room_264_partition import partition
from randomizer.entities.rooms.room.room_264.room_264_exits import exits
from randomizer.entities.rooms.room.room_264.room_264_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E1791_LANDS_END_UNDERGROUND_DOG_WALL_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
