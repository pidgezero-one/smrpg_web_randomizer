"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_94.room_94_partition import partition
from randomizer.entities.rooms.room.room_94.room_94_exits import exits
from randomizer.entities.rooms.room.room_94.room_94_objects import objects

room = Room(
    partition=partition,
    music=M18_ROSE_TOWN,
    entrance_event=E0575_ROSE_TOWN_LIBERATED_COUPLES_HOUSE_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
