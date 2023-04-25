"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_24.room_24_partition import partition
from randomizer.entities.rooms.room.room_24.room_24_exits import exits
from randomizer.entities.rooms.room.room_24.room_24_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E3280_SHIP_LOWER_HENCHMAN_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
