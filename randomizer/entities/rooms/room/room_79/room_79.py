"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_79.room_79_partition import partition
from randomizer.entities.rooms.room.room_79.room_79_exits import exits
from randomizer.entities.rooms.room.room_79.room_79_events import events
from randomizer.entities.rooms.room.room_79.room_79_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E3148_ROSE_WAY_MAIN_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
