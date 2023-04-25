"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_407.room_407_partition import partition
from randomizer.entities.rooms.room.room_407.room_407_exits import exits
from randomizer.entities.rooms.room.room_407.room_407_events import events
from randomizer.entities.rooms.room.room_407.room_407_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E1777_LANDS_END_CLIFF_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
