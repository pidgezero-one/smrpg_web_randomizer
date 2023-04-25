"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_165.room_165_partition import partition
from randomizer.entities.rooms.room.room_165.room_165_exits import exits
from randomizer.entities.rooms.room.room_165.room_165_events import events
from randomizer.entities.rooms.room.room_165.room_165_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E3226_SHIP_GENERIC_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
