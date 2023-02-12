from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_432.room_432_partition import partition
from randomizer.entities.rooms.rooms.room_432.room_432_objects import objects

room = Room(
    partition=partition,
    music=M71_ENDING_PART_2,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
