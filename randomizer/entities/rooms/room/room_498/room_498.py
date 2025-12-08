"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_498.room_498_partition import partition
from randomizer.entities.rooms.room.room_498.room_498_exits import exits
from randomizer.entities.rooms.room.room_498.room_498_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3703_NIMBUS_CASTLE_TWO_LEVEL_CHEST_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
