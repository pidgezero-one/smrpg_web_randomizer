"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_421.room_421_partition import partition
from randomizer.entities.rooms.room.room_421.room_421_exits import exits
from randomizer.entities.rooms.room.room_421.room_421_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E1770_TEMPLE_FORTUNE_RESULTS_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
