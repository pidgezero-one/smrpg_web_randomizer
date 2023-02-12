from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_410.room_410_partition import partition
from randomizer.entities.rooms.rooms.room_410.room_410_exits import exits
from randomizer.entities.rooms.rooms.room_410.room_410_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3707_NIMBUS_CASTLE_WEST_STAIRCASE_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
