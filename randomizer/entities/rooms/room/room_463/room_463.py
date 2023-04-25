"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_463.room_463_partition import partition
from randomizer.entities.rooms.room.room_463.room_463_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E3354_KEEP_BARREL_COUNT_LOADER,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.MUTE,
    ],
)
