"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_499.room_499_partition import partition
from randomizer.entities.rooms.room.room_499.room_499_exits import exits
from randomizer.entities.rooms.room.room_499.room_499_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3762_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
