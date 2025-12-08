"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_197.room_197_partition import partition
from randomizer.entities.rooms.room.room_197.room_197_exits import exits
from randomizer.entities.rooms.room.room_197.room_197_events import events
from randomizer.entities.rooms.room.room_197.room_197_objects import objects

room = Room(
    partition=partition,
    music=M31_BOOSTERS_TOWER,
    entrance_event=E2340_TOWER_SEESAW_CHEST_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SALUTE,
    ])
