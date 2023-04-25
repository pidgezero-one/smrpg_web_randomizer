"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_36.room_36_partition import partition
from randomizer.entities.rooms.room.room_36.room_36_exits import exits
from randomizer.entities.rooms.room.room_36.room_36_events import events
from randomizer.entities.rooms.room.room_36.room_36_objects import objects

room = Room(
    partition=partition,
    music=M32_AND_MY_NAMES_BOOSTER,
    entrance_event=E2344_TOWER_THWOMP_SEESAW_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
