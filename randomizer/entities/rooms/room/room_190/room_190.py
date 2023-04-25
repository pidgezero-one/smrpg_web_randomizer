"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_190.room_190_partition import partition
from randomizer.entities.rooms.room.room_190.room_190_exits import exits
from randomizer.entities.rooms.room.room_190.room_190_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0376_MUSHROOM_KINGDOM_OCCUPIED_EXTERIOR_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
