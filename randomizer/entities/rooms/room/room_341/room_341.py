"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_341.room_341_partition import partition
from randomizer.entities.rooms.room.room_341.room_341_events import events
from randomizer.entities.rooms.room.room_341.room_341_objects import objects

room = Room(
    partition=partition,
    music=M50_NIMBUS_LAND,
    entrance_event=E0737_GARROS_HOUSE_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
