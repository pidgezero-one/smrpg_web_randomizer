"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_54.room_54_partition import partition
from randomizer.entities.rooms.room.room_54.room_54_objects import objects

room = Room(
    partition=partition,
    music=M37_BOOSTER_HILL_START,
    entrance_event=E3499_BOOSTER_HILL_1ST_PASS_LOADER,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.TUMBLE_BACK,
    ],
)
