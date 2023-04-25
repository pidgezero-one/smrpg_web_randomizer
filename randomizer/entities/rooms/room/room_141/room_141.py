"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_141.room_141_partition import partition
from randomizer.entities.rooms.room.room_141.room_141_exits import exits
from randomizer.entities.rooms.room.room_141.room_141_events import events
from randomizer.entities.rooms.room.room_141.room_141_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E1780_LANDS_END_FLOWER_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
