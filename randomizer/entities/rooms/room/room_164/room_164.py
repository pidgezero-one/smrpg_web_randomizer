"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_164.room_164_partition import partition
from randomizer.entities.rooms.room.room_164.room_164_exits import exits
from randomizer.entities.rooms.room.room_164.room_164_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E3921_SHIP_FIRST_SAVE_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
