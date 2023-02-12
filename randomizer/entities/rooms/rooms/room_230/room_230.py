from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_230.room_230_partition import partition
from randomizer.entities.rooms.rooms.room_230.room_230_events import events
from randomizer.entities.rooms.rooms.room_230.room_230_objects import objects

room = Room(
    partition=partition,
    music=M26_FOREST_MAZE,
    entrance_event=E2431_FOREST_MAZE_AREA_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
