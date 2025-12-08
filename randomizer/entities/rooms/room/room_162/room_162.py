"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_162.room_162_partition import partition
from randomizer.entities.rooms.room.room_162.room_162_exits import exits
from randomizer.entities.rooms.room.room_162.room_162_events import events
from randomizer.entities.rooms.room.room_162.room_162_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E3226_SHIP_GENERIC_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
