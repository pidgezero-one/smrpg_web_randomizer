"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_414.room_414_partition import partition
from randomizer.entities.rooms.room.room_414.room_414_exits import exits
from randomizer.entities.rooms.room.room_414.room_414_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3724_NIMBUS_CASTLE_OUTER_CELLAR_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
