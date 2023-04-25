"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_233.room_233_partition import partition
from randomizer.entities.rooms.room.room_233.room_233_events import events
from randomizer.entities.rooms.room.room_233.room_233_objects import objects

room = Room(
    partition=partition,
    music=M26_FOREST_MAZE,
    entrance_event=E2418_FOREST_UNDERGROUND_1_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
