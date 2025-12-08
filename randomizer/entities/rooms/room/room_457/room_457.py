"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_457.room_457_partition import partition
from randomizer.entities.rooms.room.room_457.room_457_events import events
from randomizer.entities.rooms.room.room_457.room_457_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E1835_KEEP_CANNONBALL_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.TUMBLE_BACK,
        ExtraSpriteActions.RECOIL,
    ])
