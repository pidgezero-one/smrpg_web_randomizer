from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_115.room_115_partition import partition
from randomizer.entities.rooms.rooms.room_115.room_115_exits import exits
from randomizer.entities.rooms.rooms.room_115.room_115_objects import objects

room = Room(
    partition=partition,
    music=M61_VALENTINA,
    entrance_event=E3730_NIMBUS_CASTLE_OCCUPIED_4_PATH_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
