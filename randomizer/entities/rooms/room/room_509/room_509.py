"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_509.room_509_partition import partition
from randomizer.entities.rooms.room.room_509.room_509_objects import objects

room = Room(
    partition=partition,
    music=M56_FACTORY,
    entrance_event=E3792_FACTORY_FINAL_BOSS_ROOM_LOADER,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.CROUCH,
    ],
)
