from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_224.room_224_partition import partition
from randomizer.entities.rooms.rooms.room_224.room_224_exits import exits
from randomizer.entities.rooms.rooms.room_224.room_224_objects import objects

room = Room(
    partition=partition,
    music=M26_FOREST_MAZE,
    entrance_event=E3918_FOREST_MAZE_ENTRANCE_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
