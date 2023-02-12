from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_14.room_14_partition import partition
from randomizer.entities.rooms.rooms.room_14.room_14_objects import objects

room = Room(
    partition=partition,
    music=M37_BOOSTER_HILL_START,
    entrance_event=E3507_BOOSTER_HILL_2ND_PASS_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.TumbleBack,
    ],
)
