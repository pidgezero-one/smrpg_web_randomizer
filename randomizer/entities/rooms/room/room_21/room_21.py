"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_21.room_21_partition import partition
from randomizer.entities.rooms.room.room_21.room_21_exits import exits
from randomizer.entities.rooms.room.room_21.room_21_objects import objects

room = Room(
    partition=partition,
    music=M02_MUSHROOM_KINGDOM,
    entrance_event=E0401_GUEST_ROOM_ANTECHAMBER_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
