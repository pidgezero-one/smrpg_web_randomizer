from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_315.room_315_partition import partition
from randomizer.entities.rooms.rooms.room_315.room_315_exits import exits
from randomizer.entities.rooms.rooms.room_315.room_315_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1145_SEASIDE_OCCUPIED_BEACH_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
