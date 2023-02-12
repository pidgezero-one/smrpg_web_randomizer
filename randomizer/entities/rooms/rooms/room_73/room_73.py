from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_73.room_73_partition import partition
from randomizer.entities.rooms.rooms.room_73.room_73_objects import objects

room = Room(
    partition=partition,
    music=M22_MIDAS_RIVER,
    entrance_event=E3485_MIDAS_RIVER_BOTTOM_RIGHT_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Swim,
    ],
)
