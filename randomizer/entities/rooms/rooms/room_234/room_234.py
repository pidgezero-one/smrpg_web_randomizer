from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_234.room_234_partition import partition
from randomizer.entities.rooms.rooms.room_234.room_234_objects import objects

room = Room(
    partition=partition,
    music=M26_FOREST_MAZE,
    entrance_event=E2425_FOREST_MAZE_SECRET_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
