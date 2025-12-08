"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_189.room_189_partition import partition
from randomizer.entities.rooms.room.room_189.room_189_exits import exits
from randomizer.entities.rooms.room.room_189.room_189_events import events
from randomizer.entities.rooms.room.room_189.room_189_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1392_MARIOS_HOUSE_INTERIOR_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.FLOP,
    ])
