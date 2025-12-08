"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_285.room_285_partition import partition
from randomizer.entities.rooms.room.room_285.room_285_exits import exits
from randomizer.entities.rooms.room.room_285.room_285_events import events
from randomizer.entities.rooms.room.room_285.room_285_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.TUMBLE_FRONT,
    ])
