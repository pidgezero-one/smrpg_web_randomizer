from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_82.room_82_partition import partition
from randomizer.entities.rooms.rooms.room_82.room_82_exits import exits
from randomizer.entities.rooms.rooms.room_82.room_82_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
