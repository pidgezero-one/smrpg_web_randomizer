"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_472.room_472_partition import partition
from randomizer.entities.rooms.room.room_472.room_472_exits import exits
from randomizer.entities.rooms.room.room_472.room_472_events import events
from randomizer.entities.rooms.room.room_472.room_472_objects import objects

room = Room(
    partition=partition,
    music=M56_FACTORY,
    entrance_event=E2621_FACTORY_3RD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
