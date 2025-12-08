"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_480.room_480_partition import partition
from randomizer.entities.rooms.room.room_480.room_480_exits import exits
from randomizer.entities.rooms.room.room_480.room_480_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0393_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
