"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_312.room_312_partition import partition
from randomizer.entities.rooms.room.room_312.room_312_exits import exits
from randomizer.entities.rooms.room.room_312.room_312_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1160_SEASIDE_LIBERATED_MUSHROOM_BOY_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
