"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_166.room_166_partition import partition
from randomizer.entities.rooms.room.room_166.room_166_exits import exits
from randomizer.entities.rooms.room.room_166.room_166_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E3222_SHIP_TROOPA_PUZZLE_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
