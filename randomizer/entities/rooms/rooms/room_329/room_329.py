from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_329.room_329_partition import partition
from randomizer.entities.rooms.rooms.room_329.room_329_exits import exits
from randomizer.entities.rooms.rooms.room_329.room_329_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0767_MUSHROOM_KINGDOM_OCCUPIED_EAST_HALL_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
