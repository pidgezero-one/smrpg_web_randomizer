"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_16.room_16_partition import partition
from randomizer.entities.rooms.room.room_16.room_16_exits import exits
from randomizer.entities.rooms.room.room_16.room_16_events import events
from randomizer.entities.rooms.room.room_16.room_16_objects import objects

room = Room(
    partition=partition,
    music=M14_MARIOS_PAD,
    entrance_event=E1408_MARIOS_PAD_EXTERIOR_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
