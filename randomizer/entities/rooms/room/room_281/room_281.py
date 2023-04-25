"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_281.room_281_partition import partition
from randomizer.entities.rooms.room.room_281.room_281_exits import exits
from randomizer.entities.rooms.room.room_281.room_281_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0782_MINES_ROOM_THAT_SPLITS_TO_PA_MOLE_PATH_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
