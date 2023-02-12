from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_356.room_356_partition import partition
from randomizer.entities.rooms.rooms.room_356.room_356_exits import exits
from randomizer.entities.rooms.rooms.room_356.room_356_objects import objects

room = Room(
    partition=partition,
    music=M62_BARREL_VOLCANO,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
