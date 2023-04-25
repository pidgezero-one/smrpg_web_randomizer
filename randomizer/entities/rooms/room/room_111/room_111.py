"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_111.room_111_partition import partition
from randomizer.entities.rooms.room.room_111.room_111_exits import exits
from randomizer.entities.rooms.room.room_111.room_111_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3712_NIMBUS_CASTLE_BRIDGE_ROOM_NPC_ANIMATIONS,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
