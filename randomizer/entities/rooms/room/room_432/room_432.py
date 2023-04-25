"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_432.room_432_partition import partition
from randomizer.entities.rooms.room.room_432.room_432_objects import objects

room = Room(
    partition=partition,
    music=M71_ENDING_PART_2,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
