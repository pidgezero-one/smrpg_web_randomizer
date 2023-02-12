from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_11.room_11_partition import partition
from randomizer.entities.rooms.rooms.room_11.room_11_exits import exits
from randomizer.entities.rooms.rooms.room_11.room_11_objects import objects

room = Room(
    partition=partition,
    music=M39_MARRYMORE,
    entrance_event=E0608_MARRYMORE_INN_3F_HALLWAY_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
