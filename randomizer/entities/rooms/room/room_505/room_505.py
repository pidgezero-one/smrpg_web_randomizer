"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_505.room_505_partition import partition
from randomizer.entities.rooms.room.room_505.room_505_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3807_ENDING_CREDITS_RACE_LOADER,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
