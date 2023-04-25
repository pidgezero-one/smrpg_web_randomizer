"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_379.room_379_partition import partition
from randomizer.entities.rooms.room.room_379.room_379_exits import exits
from randomizer.entities.rooms.room.room_379.room_379_events import events
from randomizer.entities.rooms.room.room_379.room_379_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.CLIMB,
    ],
)
