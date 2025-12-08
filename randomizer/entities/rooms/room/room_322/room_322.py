"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_322.room_322_partition import partition
from randomizer.entities.rooms.room.room_322.room_322_events import events
from randomizer.entities.rooms.room.room_322.room_322_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E1826_KEEP_INVISIBLE_FLOOR_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.RECOIL,
    ])
