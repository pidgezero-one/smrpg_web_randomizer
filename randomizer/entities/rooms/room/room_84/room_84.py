"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_84.room_84_partition import partition
from randomizer.entities.rooms.room.room_84.room_84_exits import exits
from randomizer.entities.rooms.room.room_84.room_84_events import events
from randomizer.entities.rooms.room.room_84.room_84_objects import objects

room = Room(
    partition=partition,
    music=M18_ROSE_TOWN,
    entrance_event=E0556_ROSE_TOWN_LIBERATED_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DOWN_PIPE,
    ])
