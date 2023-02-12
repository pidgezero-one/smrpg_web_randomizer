from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_374.room_374_partition import partition
from randomizer.entities.rooms.rooms.room_374.room_374_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SurpriseFrame,
    ],
)
