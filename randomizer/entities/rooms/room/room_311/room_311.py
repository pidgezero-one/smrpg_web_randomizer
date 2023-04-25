"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_311.room_311_partition import partition
from randomizer.entities.rooms.room.room_311.room_311_exits import exits
from randomizer.entities.rooms.room.room_311.room_311_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1159_SEASIDE_LIBERATED_HEALTH_STORE_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
