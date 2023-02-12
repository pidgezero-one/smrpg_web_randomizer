from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_345.room_345_partition import partition
from randomizer.entities.rooms.rooms.room_345.room_345_events import events
from randomizer.entities.rooms.rooms.room_345.room_345_objects import objects

room = Room(
    partition=partition,
    music=M50_NIMBUS_LAND,
    entrance_event=E0724_NIMBUS_CROCO_HOUSE_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
