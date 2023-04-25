"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_88.room_88_partition import partition
from randomizer.entities.rooms.room.room_88.room_88_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.LOOK_AT_DOLL,
        ExtraSpriteActions.PRAISE_FRONT,
    ],
)
