"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_366.room_366_partition import partition
from randomizer.entities.rooms.room.room_366.room_366_exits import exits
from randomizer.entities.rooms.room.room_366.room_366_objects import objects

room = Room(
    partition=partition,
    music=M62_BARREL_VOLCANO,
    entrance_event=E3923_VOLCANO_SAVE_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
