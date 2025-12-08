"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_363.room_363_partition import partition
from randomizer.entities.rooms.room.room_363.room_363_exits import exits
from randomizer.entities.rooms.room.room_363.room_363_objects import objects

room = Room(
    partition=partition,
    music=M62_BARREL_VOLCANO,
    entrance_event=E3336_CORKPEDITE_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
