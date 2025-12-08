"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_381.room_381_partition import partition
from randomizer.entities.rooms.room.room_381.room_381_exits import exits
from randomizer.entities.rooms.room.room_381.room_381_events import events
from randomizer.entities.rooms.room.room_381.room_381_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.CLIMB,
    ])
