"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_316.room_316_partition import partition
from randomizer.entities.rooms.room.room_316.room_316_exits import exits
from randomizer.entities.rooms.room.room_316.room_316_objects import objects

room = Room(
    partition=partition,
    music=M05_SEASIDE_TOWN,
    entrance_event=E1163_SEASIDE_LIBERATED_BEACH,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
