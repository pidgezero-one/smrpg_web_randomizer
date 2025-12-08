"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_497.room_497_partition import partition
from randomizer.entities.rooms.room.room_497.room_497_exits import exits
from randomizer.entities.rooms.room.room_497.room_497_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0833_NIMBUS_CASTLE_LIBERATED_INNER_CELLAR_HALLWAY_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
