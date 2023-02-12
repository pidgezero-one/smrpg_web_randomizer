from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_354.room_354_partition import partition
from randomizer.entities.rooms.rooms.room_354.room_354_exits import exits
from randomizer.entities.rooms.rooms.room_354.room_354_objects import objects

room = Room(
    partition=partition,
    music=M62_BARREL_VOLCANO,
    entrance_event=E3323_VOLCANO_1ST_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
