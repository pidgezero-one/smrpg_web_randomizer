from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_216.room_216_partition import partition
from randomizer.entities.rooms.rooms.room_216.room_216_exits import exits
from randomizer.entities.rooms.rooms.room_216.room_216_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E1128_SEASIDE_OCCUPIED_MUSHROOM_BOY_SHOP_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
