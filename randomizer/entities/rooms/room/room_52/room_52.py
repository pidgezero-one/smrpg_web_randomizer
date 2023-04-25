"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_52.room_52_partition import partition
from randomizer.entities.rooms.room.room_52.room_52_exits import exits
from randomizer.entities.rooms.room.room_52.room_52_events import events
from randomizer.entities.rooms.room.room_52.room_52_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0747_MUSHROOM_KINGDOM_INN_2F_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SLEEP,
    ],
)
