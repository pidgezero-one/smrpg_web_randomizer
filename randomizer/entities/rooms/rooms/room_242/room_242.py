from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_242.room_242_partition import partition
from randomizer.entities.rooms.rooms.room_242.room_242_events import events
from randomizer.entities.rooms.rooms.room_242.room_242_objects import objects

room = Room(
    partition=partition,
    music=M26_FOREST_MAZE,
    entrance_event=E2418_FOREST_UNDERGROUND_1_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SurpriseFrame,
    ],
)
