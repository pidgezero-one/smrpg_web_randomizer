"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_273.room_273_partition import partition
from randomizer.entities.rooms.room.room_273.room_273_exits import exits
from randomizer.entities.rooms.room.room_273.room_273_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0776_MINES_TRAMPOLINE_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.RECOIL,
        ExtraSpriteActions.DIZZY,
        ExtraSpriteActions.FLOP,
    ],
)
