"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_226.room_226_partition import partition
from randomizer.entities.rooms.room.room_226.room_226_exits import exits
from randomizer.entities.rooms.room.room_226.room_226_events import events
from randomizer.entities.rooms.room.room_226.room_226_objects import objects

room = Room(
    partition=partition,
    music=M26_FOREST_MAZE,
    entrance_event=E1554_FOREST_FIRST_WIGGLER_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DOWN_PIPE,
    ])
