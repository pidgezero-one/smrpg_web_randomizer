"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_169.room_169_partition import partition
from randomizer.entities.rooms.room.room_169.room_169_exits import exits
from randomizer.entities.rooms.room.room_169.room_169_events import events
from randomizer.entities.rooms.room.room_169.room_169_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
