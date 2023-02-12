from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_501.room_501_partition import partition
from randomizer.entities.rooms.rooms.room_501.room_501_exits import exits
from randomizer.entities.rooms.rooms.room_501.room_501_objects import objects

room = Room(
    partition=partition,
    music=M50_NIMBUS_LAND,
    entrance_event=E0837_NIMBUS_CASTLE_LIBERATED_4WAY_PATH_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
