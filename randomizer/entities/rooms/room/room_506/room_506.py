"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_506.room_506_partition import partition
from randomizer.entities.rooms.room.room_506.room_506_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E2294_ENDING_CREDITS_WEDDING_LOADER,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
