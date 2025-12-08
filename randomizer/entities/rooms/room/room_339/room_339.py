"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_339.room_339_partition import partition
from randomizer.entities.rooms.room.room_339.room_339_events import events
from randomizer.entities.rooms.room.room_339.room_339_objects import objects

room = Room(
    partition=partition,
    music=M33_MOLEVILLE,
    entrance_event=E1871_FIREWORKS_HOUSE_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[])
