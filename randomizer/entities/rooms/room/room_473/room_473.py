"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_473.room_473_partition import partition
from randomizer.entities.rooms.room.room_473.room_473_exits import exits
from randomizer.entities.rooms.room.room_473.room_473_events import events
from randomizer.entities.rooms.room.room_473.room_473_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
