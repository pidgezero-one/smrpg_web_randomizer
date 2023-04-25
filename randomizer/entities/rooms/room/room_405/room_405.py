"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_405.room_405_partition import partition
from randomizer.entities.rooms.room.room_405.room_405_events import events
from randomizer.entities.rooms.room.room_405.room_405_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E2570_BOOSTER_PASS_SECRET_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
