"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_6.room_6_partition import partition
from randomizer.entities.rooms.room.room_6.room_6_exits import exits
from randomizer.entities.rooms.room.room_6.room_6_objects import objects

room = Room(
    partition=partition,
    music=M39_MARRYMORE,
    entrance_event=E0612_MARRYMORE_INN_2F_HALLWAY_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DOWN_PIPE,
    ],
)
