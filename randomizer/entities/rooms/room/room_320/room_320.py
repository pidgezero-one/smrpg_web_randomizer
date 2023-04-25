"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_320.room_320_partition import partition
from randomizer.entities.rooms.room.room_320.room_320_exits import exits
from randomizer.entities.rooms.room.room_320.room_320_events import events
from randomizer.entities.rooms.room.room_320.room_320_objects import objects

room = Room(
    partition=partition,
    music=M02_MUSHROOM_KINGDOM,
    entrance_event=E0257_FADE_IN_ASYNC,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
