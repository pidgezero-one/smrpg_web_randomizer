from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_314.room_314_partition import partition
from randomizer.entities.rooms.rooms.room_314.room_314_exits import exits
from randomizer.entities.rooms.rooms.room_314.room_314_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1162_SEASIDE_LIBERATED_SHED_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
