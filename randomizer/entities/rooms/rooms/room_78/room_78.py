from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_78.room_78_partition import partition
from randomizer.entities.rooms.rooms.room_78.room_78_exits import exits
from randomizer.entities.rooms.rooms.room_78.room_78_objects import objects

room = Room(
    partition=partition,
    music=M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
    entrance_event=E1698_BANDITS_WAY_4_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
