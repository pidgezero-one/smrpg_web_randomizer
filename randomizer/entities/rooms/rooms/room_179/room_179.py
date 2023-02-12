from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_179.room_179_partition import partition
from randomizer.entities.rooms.rooms.room_179.room_179_exits import exits
from randomizer.entities.rooms.rooms.room_179.room_179_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E3227_SHIP_CLONE_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
