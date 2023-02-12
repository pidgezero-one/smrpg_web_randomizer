from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_368.room_368_partition import partition
from randomizer.entities.rooms.rooms.room_368.room_368_events import events
from randomizer.entities.rooms.rooms.room_368.room_368_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3677_ROYAL_BUS_PLATFORM_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
