"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_22.room_22_partition import partition
from randomizer.entities.rooms.room.room_22.room_22_exits import exits
from randomizer.entities.rooms.room.room_22.room_22_events import events
from randomizer.entities.rooms.room.room_22.room_22_objects import objects

room = Room(
    partition=partition,
    music=M02_MUSHROOM_KINGDOM,
    entrance_event=E3814_MUSHROOM_KINGDOM_LIBERATED_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
