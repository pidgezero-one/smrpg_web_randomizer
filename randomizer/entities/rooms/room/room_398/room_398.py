"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_398.room_398_partition import partition
from randomizer.entities.rooms.room.room_398.room_398_exits import exits
from randomizer.entities.rooms.room.room_398.room_398_objects import objects

room = Room(
    partition=partition,
    music=M51_MONSTRO_TOWN,
    entrance_event=E2051_MONSTRO_SHOP_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
