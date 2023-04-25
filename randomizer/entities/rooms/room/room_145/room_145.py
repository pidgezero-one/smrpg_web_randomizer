"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_145.room_145_partition import partition
from randomizer.entities.rooms.room.room_145.room_145_events import events
from randomizer.entities.rooms.room.room_145.room_145_objects import objects

room = Room(
    partition=partition,
    music=M34_STAR_HILL,
    entrance_event=E2793_STAR_HILL_ENTRANCE_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
