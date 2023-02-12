from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_467.room_467_partition import partition
from randomizer.entities.rooms.rooms.room_467.room_467_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Mute,
    ],
)
