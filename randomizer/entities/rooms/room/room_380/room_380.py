"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_380.room_380_partition import partition
from randomizer.entities.rooms.room.room_380.room_380_exits import exits
from randomizer.entities.rooms.room.room_380.room_380_events import events
from randomizer.entities.rooms.room.room_380.room_380_objects import objects

room = Room(
    partition=partition,
    music=M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.CLIMB,
    ],
)
