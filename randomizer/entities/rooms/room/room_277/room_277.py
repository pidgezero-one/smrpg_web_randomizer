"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_277.room_277_partition import partition
from randomizer.entities.rooms.room.room_277.room_277_exits import exits
from randomizer.entities.rooms.room.room_277.room_277_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0778_MINES_LEFT_OF_TRAMPOLINE_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
