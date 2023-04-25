"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_387.room_387_partition import partition
from randomizer.entities.rooms.room.room_387.room_387_exits import exits
from randomizer.entities.rooms.room.room_387.room_387_objects import objects

room = Room(
    partition=partition,
    music=M62_BARREL_VOLCANO,
    entrance_event=E3923_VOLCANO_SAVE_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
