from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_235.room_235_partition import partition
from randomizer.entities.rooms.rooms.room_235.room_235_exits import exits
from randomizer.entities.rooms.rooms.room_235.room_235_events import events
from randomizer.entities.rooms.rooms.room_235.room_235_objects import objects

room = Room(
    partition=partition,
    music=M26_FOREST_MAZE,
    entrance_event=E2418_FOREST_UNDERGROUND_1_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
