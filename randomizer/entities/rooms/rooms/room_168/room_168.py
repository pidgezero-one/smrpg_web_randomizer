from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_168.room_168_partition import partition
from randomizer.entities.rooms.rooms.room_168.room_168_exits import exits
from randomizer.entities.rooms.rooms.room_168.room_168_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E3211_SHIP_3D_MAZE_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
