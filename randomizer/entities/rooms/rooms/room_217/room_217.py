from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_217.room_217_partition import partition
from randomizer.entities.rooms.rooms.room_217.room_217_exits import exits
from randomizer.entities.rooms.rooms.room_217.room_217_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E1129_SEASIDE_OCCUPIED_ACCESSORY_SHOP_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
