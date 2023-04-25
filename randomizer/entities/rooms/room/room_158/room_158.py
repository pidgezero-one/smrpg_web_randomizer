"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_158.room_158_partition import partition
from randomizer.entities.rooms.room.room_158.room_158_events import events
from randomizer.entities.rooms.room.room_158.room_158_objects import objects

room = Room(
    partition=partition,
    music=M34_STAR_HILL,
    entrance_event=E2526_STAR_HILL_1ST_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
