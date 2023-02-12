from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_313.room_313_partition import partition
from randomizer.entities.rooms.rooms.room_313.room_313_exits import exits
from randomizer.entities.rooms.rooms.room_313.room_313_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1161_SEASIDE_LIBERATED_ACCESSORY_SHOP_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
