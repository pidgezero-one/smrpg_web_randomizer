"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_92.room_92_partition import partition
from randomizer.entities.rooms.room.room_92.room_92_exits import exits
from randomizer.entities.rooms.room.room_92.room_92_objects import objects

room = Room(
    partition=partition,
    music=M47_GRATE_GUYS_CASINO,
    entrance_event=E2633_CASINO_INTERIOR_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.RECOIL,
        ExtraSpriteActions.BLACKJACK,
    ],
)
