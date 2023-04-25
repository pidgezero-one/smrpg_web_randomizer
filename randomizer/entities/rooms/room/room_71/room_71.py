"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_71.room_71_partition import partition
from randomizer.entities.rooms.room.room_71.room_71_objects import objects

room = Room(
    partition=partition,
    music=M22_MIDAS_RIVER,
    entrance_event=E3483_MIDAS_RIVER_MID_LEFT_OR_MID_RIGHT_LOADER,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SWIM,
    ],
)
