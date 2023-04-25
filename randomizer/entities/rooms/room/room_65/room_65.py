"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_65.room_65_partition import partition
from randomizer.entities.rooms.room.room_65.room_65_events import events
from randomizer.entities.rooms.room.room_65.room_65_objects import objects

room = Room(
    partition=partition,
    music=M39_MARRYMORE,
    entrance_event=E0677_MARRYMORE_UNOCCUPIED_SANCTUARY_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
