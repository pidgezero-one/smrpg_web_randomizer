"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_455.room_455_partition import partition
from randomizer.entities.rooms.room.room_455.room_455_events import events
from randomizer.entities.rooms.room.room_455.room_455_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E1825_KEEP_ROTATING_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.RECOIL,
        ExtraSpriteActions.WOBBLE,
    ],
)
