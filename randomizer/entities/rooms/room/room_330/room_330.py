"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_330.room_330_partition import partition
from randomizer.entities.rooms.room.room_330.room_330_exits import exits
from randomizer.entities.rooms.room.room_330.room_330_events import events
from randomizer.entities.rooms.room.room_330.room_330_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
