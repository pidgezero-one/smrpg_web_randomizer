"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_302.room_302_partition import partition
from randomizer.entities.rooms.room.room_302.room_302_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E0773_KERO_SEWERS_BELOME_ROOM_LOADER_CONTAINER,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
