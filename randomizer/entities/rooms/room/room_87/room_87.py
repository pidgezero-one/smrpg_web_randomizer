"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_87.room_87_partition import partition
from randomizer.entities.rooms.room.room_87.room_87_events import events
from randomizer.entities.rooms.room.room_87.room_87_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0261_FADE_MUSIC_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[])
