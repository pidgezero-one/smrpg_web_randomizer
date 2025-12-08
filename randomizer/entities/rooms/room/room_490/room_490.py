"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_490.room_490_partition import partition
from randomizer.entities.rooms.room.room_490.room_490_exits import exits
from randomizer.entities.rooms.room.room_490.room_490_events import events
from randomizer.entities.rooms.room.room_490.room_490_objects import objects

room = Room(
    partition=partition,
    music=M02_MUSHROOM_KINGDOM,
    entrance_event=E0344_MUSHROOM_KINGDOM_RAZ_RAINI_HOUSE_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
