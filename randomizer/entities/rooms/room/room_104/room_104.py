"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_104.room_104_partition import partition
from randomizer.entities.rooms.room.room_104.room_104_exits import exits
from randomizer.entities.rooms.room.room_104.room_104_objects import objects

room = Room(
    partition=partition,
    music=M47_GRATE_GUYS_CASINO,
    entrance_event=E2635_CASINO_DOORWAY_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
