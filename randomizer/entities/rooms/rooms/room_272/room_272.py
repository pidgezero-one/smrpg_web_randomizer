from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_272.room_272_partition import partition
from randomizer.entities.rooms.rooms.room_272.room_272_exits import exits
from randomizer.entities.rooms.rooms.room_272.room_272_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
