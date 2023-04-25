"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_310.room_310_partition import partition
from randomizer.entities.rooms.room.room_310.room_310_exits import exits
from randomizer.entities.rooms.room.room_310.room_310_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1158_SEASIDE_LIBERATED_WPN_ARM_SHOP_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
