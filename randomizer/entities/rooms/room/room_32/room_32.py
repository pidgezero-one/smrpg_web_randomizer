"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_32.room_32_partition import partition
from randomizer.entities.rooms.room.room_32.room_32_exits import exits
from randomizer.entities.rooms.room.room_32.room_32_objects import objects

room = Room(
    partition=partition,
    music=M02_MUSHROOM_KINGDOM,
    entrance_event=E0319_TOADSTOOL_ANTECHAMBER_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
