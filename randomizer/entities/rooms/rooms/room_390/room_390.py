from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_390.room_390_partition import partition
from randomizer.entities.rooms.rooms.room_390.room_390_exits import exits
from randomizer.entities.rooms.rooms.room_390.room_390_objects import objects

room = Room(
    partition=partition,
    music=M62_BARREL_VOLCANO,
    entrance_event=E3325_STUMPET_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
