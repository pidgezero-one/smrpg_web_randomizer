"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_467.room_467_partition import partition
from randomizer.entities.rooms.room.room_467.room_467_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.MUTE,
    ])
