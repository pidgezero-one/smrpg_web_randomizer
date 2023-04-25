"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_327.room_327_partition import partition
from randomizer.entities.rooms.room.room_327.room_327_exits import exits
from randomizer.entities.rooms.room.room_327.room_327_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0391_MUSHROOM_KINGDOM_OCCUPIED_LEFT_STAIRWAY_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
