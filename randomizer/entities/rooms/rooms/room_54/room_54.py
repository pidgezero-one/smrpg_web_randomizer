from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_54.room_54_partition import partition
from randomizer.entities.rooms.rooms.room_54.room_54_objects import objects

room = Room(
    partition=partition,
    music=M37_BOOSTER_HILL_START,
    entrance_event=E3499_BOOSTER_HILL_1ST_PASS_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.TumbleBack,
    ],
)
