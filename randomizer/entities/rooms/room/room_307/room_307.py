"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_307.room_307_partition import partition
from randomizer.entities.rooms.room.room_307.room_307_exits import exits
from randomizer.entities.rooms.room.room_307.room_307_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1155_SEASIDE_LIBERATED_ELDERS_HOUSE_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
