"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_201.room_201_partition import partition
from randomizer.entities.rooms.room.room_201.room_201_exits import exits
from randomizer.entities.rooms.room.room_201.room_201_events import events
from randomizer.entities.rooms.room.room_201.room_201_objects import objects

room = Room(
    partition=partition,
    music=M32_AND_MY_NAMES_BOOSTER,
    entrance_event=E2445_TOWER_SMALL_SAVE_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
