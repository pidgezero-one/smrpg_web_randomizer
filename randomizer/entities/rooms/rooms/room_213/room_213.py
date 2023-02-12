from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_213.room_213_partition import partition
from randomizer.entities.rooms.rooms.room_213.room_213_exits import exits
from randomizer.entities.rooms.rooms.room_213.room_213_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1125_SEASIDE_OCCUPIED_BOMB_SHOP_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
