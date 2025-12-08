"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_118.room_118_partition import partition
from randomizer.entities.rooms.room.room_118.room_118_exits import exits
from randomizer.entities.rooms.room.room_118.room_118_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3704_NIMBUS_CASTLE_OCCUPIED_5_DOOR_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
