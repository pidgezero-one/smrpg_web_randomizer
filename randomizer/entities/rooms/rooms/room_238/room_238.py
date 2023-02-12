from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_238.room_238_partition import partition
from randomizer.entities.rooms.rooms.room_238.room_238_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E2360_ABYSS_1ST_TRAMPOLINE_CATCHER_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SurpriseFrame,
    ],
)
