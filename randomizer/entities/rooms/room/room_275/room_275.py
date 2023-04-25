"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_275.room_275_partition import partition
from randomizer.entities.rooms.room.room_275.room_275_exits import exits
from randomizer.entities.rooms.room.room_275.room_275_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
