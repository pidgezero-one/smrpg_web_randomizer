from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_171.room_171_partition import partition
from randomizer.entities.rooms.rooms.room_171.room_171_exits import exits
from randomizer.entities.rooms.rooms.room_171.room_171_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
