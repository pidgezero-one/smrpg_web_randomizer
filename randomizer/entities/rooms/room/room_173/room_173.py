"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_173.room_173_partition import partition
from randomizer.entities.rooms.room.room_173.room_173_exits import exits
from randomizer.entities.rooms.room.room_173.room_173_events import events
from randomizer.entities.rooms.room.room_173.room_173_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E0879_SHIP_TRAMPOLINE_LOADER_OVERRIDE,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
