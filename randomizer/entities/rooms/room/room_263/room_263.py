"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_263.room_263_partition import partition
from randomizer.entities.rooms.room.room_263.room_263_exits import exits
from randomizer.entities.rooms.room.room_263.room_263_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E1779_LANDS_END_UNDERGROUND_1_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
