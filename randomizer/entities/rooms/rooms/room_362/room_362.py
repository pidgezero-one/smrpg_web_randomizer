from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_362.room_362_partition import partition
from randomizer.entities.rooms.rooms.room_362.room_362_exits import exits
from randomizer.entities.rooms.rooms.room_362.room_362_objects import objects

room = Room(
    partition=partition,
    music=M62_BARREL_VOLCANO,
    entrance_event=E3336_CORKPEDITE_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
