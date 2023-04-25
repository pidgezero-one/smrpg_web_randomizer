"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_372.room_372_partition import partition
from randomizer.entities.rooms.room.room_372.room_372_events import events
from randomizer.entities.rooms.room.room_372.room_372_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.EXOR,
    ],
)
