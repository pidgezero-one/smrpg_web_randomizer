"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_17.room_17_partition import partition
from randomizer.entities.rooms.room.room_17.room_17_exits import exits
from randomizer.entities.rooms.room.room_17.room_17_events import events
from randomizer.entities.rooms.room.room_17.room_17_objects import objects

room = Room(
    partition=partition,
    music=M02_MUSHROOM_KINGDOM,
    entrance_event=E0320_MUSHROOM_KINGDOM_MAIN_HALL_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
