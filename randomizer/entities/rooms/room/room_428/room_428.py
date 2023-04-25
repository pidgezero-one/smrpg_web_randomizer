"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_428.room_428_partition import partition
from randomizer.entities.rooms.room.room_428.room_428_exits import exits
from randomizer.entities.rooms.room.room_428.room_428_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E1778_TEMPLE_GENERIC_PIPE_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
