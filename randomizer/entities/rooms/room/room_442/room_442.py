"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_442.room_442_partition import partition
from randomizer.entities.rooms.room.room_442.room_442_exits import exits
from randomizer.entities.rooms.room.room_442.room_442_events import events
from randomizer.entities.rooms.room.room_442.room_442_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
