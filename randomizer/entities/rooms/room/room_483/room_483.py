"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_483.room_483_partition import partition
from randomizer.entities.rooms.room.room_483.room_483_exits import exits
from randomizer.entities.rooms.room.room_483.room_483_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0404_MUSHROOM_KINGDOM_OCCUPIED_SHOP_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
