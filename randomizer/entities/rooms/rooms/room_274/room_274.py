from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_274.room_274_partition import partition
from randomizer.entities.rooms.rooms.room_274.room_274_exits import exits
from randomizer.entities.rooms.rooms.room_274.room_274_events import events
from randomizer.entities.rooms.rooms.room_274.room_274_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
