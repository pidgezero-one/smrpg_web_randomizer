from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_500.room_500_partition import partition
from randomizer.entities.rooms.rooms.room_500.room_500_exits import exits
from randomizer.entities.rooms.rooms.room_500.room_500_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3769_NIMBUS_CASTLE_LIBERATED_BRIDGE_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
