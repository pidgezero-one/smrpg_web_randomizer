"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_283.room_283_partition import partition
from randomizer.entities.rooms.room.room_283.room_283_exits import exits
from randomizer.entities.rooms.room.room_283.room_283_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0786_MINES_LONG_ROOM_IN_MINIBOSS_PATH_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
