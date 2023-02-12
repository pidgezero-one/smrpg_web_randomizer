from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_39.room_39_partition import partition
from randomizer.entities.rooms.rooms.room_39.room_39_exits import exits
from randomizer.entities.rooms.rooms.room_39.room_39_objects import objects

room = Room(
    partition=partition,
    music=M32_AND_MY_NAMES_BOOSTER,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
