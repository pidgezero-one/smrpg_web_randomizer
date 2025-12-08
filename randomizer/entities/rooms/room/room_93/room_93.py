"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_93.room_93_partition import partition
from randomizer.entities.rooms.room.room_93.room_93_exits import exits
from randomizer.entities.rooms.room.room_93.room_93_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0580_ROSE_TOWN_OCCUPIED_TREASURE_HOUSE_1F_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
