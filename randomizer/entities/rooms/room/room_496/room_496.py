"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_496.room_496_partition import partition
from randomizer.entities.rooms.room.room_496.room_496_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3797_ENDING_CREDITS_ROOM_LOADER,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.HOLD_STAR,
        ExtraSpriteActions.LEAN_BACK,
    ],
)
