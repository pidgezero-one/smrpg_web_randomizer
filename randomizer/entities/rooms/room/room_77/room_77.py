"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_77.room_77_partition import partition
from randomizer.entities.rooms.room.room_77.room_77_exits import exits
from randomizer.entities.rooms.room.room_77.room_77_objects import objects

room = Room(
    partition=partition,
    music=M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
    entrance_event=E1713_BANDITS_WAY_3_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
