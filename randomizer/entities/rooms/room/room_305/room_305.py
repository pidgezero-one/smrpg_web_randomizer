"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_305.room_305_partition import partition
from randomizer.entities.rooms.room.room_305.room_305_exits import exits
from randomizer.entities.rooms.room.room_305.room_305_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1153_SEASIDE_LIBERATED_INN_1F_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SALUTE,
    ],
)
