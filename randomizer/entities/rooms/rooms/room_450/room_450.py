from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_450.room_450_partition import partition
from randomizer.entities.rooms.rooms.room_450.room_450_exits import exits
from randomizer.entities.rooms.rooms.room_450.room_450_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
