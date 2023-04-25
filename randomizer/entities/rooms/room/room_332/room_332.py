"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_332.room_332_partition import partition
from randomizer.entities.rooms.room.room_332.room_332_exits import exits
from randomizer.entities.rooms.room.room_332.room_332_events import events
from randomizer.entities.rooms.room.room_332.room_332_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0384_MUSHROOM_KINGDOM_OCCUPIED_TOADSTOOLS_ROOM_ANTECHAMBER_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
