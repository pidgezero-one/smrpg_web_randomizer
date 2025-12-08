"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_132.room_132_partition import partition
from randomizer.entities.rooms.room.room_132.room_132_exits import exits
from randomizer.entities.rooms.room.room_132.room_132_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E3920_SEA_SAVE_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
