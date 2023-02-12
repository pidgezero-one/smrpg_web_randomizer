from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_409.room_409_partition import partition
from randomizer.entities.rooms.rooms.room_409.room_409_events import events
from randomizer.entities.rooms.rooms.room_409.room_409_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3679_NIMBUS_CASTLE_EGG_ROOM_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
