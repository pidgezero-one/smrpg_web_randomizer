"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_191.room_191_partition import partition
from randomizer.entities.rooms.room.room_191.room_191_exits import exits
from randomizer.entities.rooms.room.room_191.room_191_objects import objects

room = Room(
    partition=partition,
    music=M02_MUSHROOM_KINGDOM,
    entrance_event=E0723_MUSHROOM_KINGDOM_UNOCCUPIED_EXTERIOR_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.FLOP,
        ExtraSpriteActions.DIZZY,
    ],
)
