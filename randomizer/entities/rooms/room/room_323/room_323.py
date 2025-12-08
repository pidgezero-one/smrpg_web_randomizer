"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_323.room_323_partition import partition
from randomizer.entities.rooms.room.room_323.room_323_exits import exits
from randomizer.entities.rooms.room.room_323.room_323_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0764_MUSHROOM_KINGDOM_OCCUPIED_THRONE_ANTECHAMBER_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
