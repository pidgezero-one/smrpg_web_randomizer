"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_138.room_138_partition import partition
from randomizer.entities.rooms.room.room_138.room_138_exits import exits
from randomizer.entities.rooms.room.room_138.room_138_events import events
from randomizer.entities.rooms.room.room_138.room_138_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E1567_LANDS_END_2_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
