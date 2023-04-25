"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_458.room_458_partition import partition
from randomizer.entities.rooms.room.room_458.room_458_events import events
from randomizer.entities.rooms.room.room_458.room_458_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E1827_KEEP_LINEAR_PLATFORM_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.WOBBLE,
        ExtraSpriteActions.RECOIL,
    ],
)
