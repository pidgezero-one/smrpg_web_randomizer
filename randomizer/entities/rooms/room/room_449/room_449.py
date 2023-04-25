"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_449.room_449_partition import partition
from randomizer.entities.rooms.room.room_449.room_449_exits import exits
from randomizer.entities.rooms.room.room_449.room_449_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E3373_KEEP_THWOMP_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.FLOP,
    ],
)
