"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_160.room_160_partition import partition
from randomizer.entities.rooms.room.room_160.room_160_exits import exits
from randomizer.entities.rooms.room.room_160.room_160_events import events
from randomizer.entities.rooms.room.room_160.room_160_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E3226_SHIP_GENERIC_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
