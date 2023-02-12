from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_236.room_236_partition import partition
from randomizer.entities.rooms.rooms.room_236.room_236_exits import exits
from randomizer.entities.rooms.rooms.room_236.room_236_events import events
from randomizer.entities.rooms.rooms.room_236.room_236_objects import objects

room = Room(
    partition=partition,
    music=M26_FOREST_MAZE,
    entrance_event=E2418_FOREST_UNDERGROUND_1_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
