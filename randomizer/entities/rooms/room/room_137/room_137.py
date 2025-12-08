"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_137.room_137_partition import partition
from randomizer.entities.rooms.room.room_137.room_137_exits import exits
from randomizer.entities.rooms.room.room_137.room_137_events import events
from randomizer.entities.rooms.room.room_137.room_137_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E3819_LANDS_END_FIRST_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
