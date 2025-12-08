"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_270.room_270_partition import partition
from randomizer.entities.rooms.room.room_270.room_270_exits import exits
from randomizer.entities.rooms.room.room_270.room_270_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E1676_LANDS_END_GROTTO_ROOM_1_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
