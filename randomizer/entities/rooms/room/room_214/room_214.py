"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_214.room_214_partition import partition
from randomizer.entities.rooms.room.room_214.room_214_exits import exits
from randomizer.entities.rooms.room.room_214.room_214_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E1126_SEASIDE_OCCUPIED_ARMOR_SHOP_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
