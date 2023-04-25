"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_452.room_452_partition import partition
from randomizer.entities.rooms.room.room_452.room_452_exits import exits
from randomizer.entities.rooms.room.room_452.room_452_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E3924_KEEP_1ST_SAVE_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
