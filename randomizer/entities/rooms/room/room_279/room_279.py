"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_279.room_279_partition import partition
from randomizer.entities.rooms.room.room_279.room_279_exits import exits
from randomizer.entities.rooms.room.room_279.room_279_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0784_MINES_SMALL_NORTH_ROOM_IN_MINIBOSS_PATH_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
