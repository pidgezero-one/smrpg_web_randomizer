from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_122.room_122_partition import partition
from randomizer.entities.rooms.rooms.room_122.room_122_events import events
from randomizer.entities.rooms.rooms.room_122.room_122_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3726_NIMBUS_CASTLE_ANTECHAMBER_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
