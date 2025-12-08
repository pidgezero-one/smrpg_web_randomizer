"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_255.room_255_partition import partition
from randomizer.entities.rooms.room.room_255.room_255_exits import exits
from randomizer.entities.rooms.room.room_255.room_255_objects import objects

room = Room(
    partition=partition,
    music=M51_MONSTRO_TOWN,
    entrance_event=E2064_DOJO_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.CHALLENGE,
    ])
