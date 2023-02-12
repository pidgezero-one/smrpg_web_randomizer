from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_72.room_72_partition import partition
from randomizer.entities.rooms.rooms.room_72.room_72_objects import objects

room = Room(
    partition=partition,
    music=M22_MIDAS_RIVER,
    entrance_event=E3484_MIDAS_RIVER_BOTTOM_LEFT_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Swim,
    ],
)
