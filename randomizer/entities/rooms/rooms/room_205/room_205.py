from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_205.room_205_partition import partition
from randomizer.entities.rooms.rooms.room_205.room_205_exits import exits
from randomizer.entities.rooms.rooms.room_205.room_205_events import events
from randomizer.entities.rooms.rooms.room_205.room_205_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E2814_MUSHROOM_WAY_3_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
