"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_206.room_206_partition import partition
from randomizer.entities.rooms.room.room_206.room_206_exits import exits
from randomizer.entities.rooms.room.room_206.room_206_objects import objects

room = Room(
    partition=partition,
    music=M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
    entrance_event=E1708_BANDITS_WAY_5_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
