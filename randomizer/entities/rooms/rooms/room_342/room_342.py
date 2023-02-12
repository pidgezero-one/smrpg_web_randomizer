from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_342.room_342_partition import partition
from randomizer.entities.rooms.rooms.room_342.room_342_events import events
from randomizer.entities.rooms.rooms.room_342.room_342_objects import objects

room = Room(
    partition=partition,
    music=M50_NIMBUS_LAND,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
