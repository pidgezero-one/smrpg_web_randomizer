"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_425.room_425_partition import partition
from randomizer.entities.rooms.room.room_425.room_425_exits import exits
from randomizer.entities.rooms.room.room_425.room_425_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E1811_TEMPLE_FOUR_CHEST_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
