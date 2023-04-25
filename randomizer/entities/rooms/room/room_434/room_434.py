"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_434.room_434_partition import partition
from randomizer.entities.rooms.room.room_434.room_434_exits import exits
from randomizer.entities.rooms.room.room_434.room_434_events import events
from randomizer.entities.rooms.room.room_434.room_434_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E1888_ABYSS_AXEM_PIT_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
