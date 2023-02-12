from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_344.room_344_partition import partition
from randomizer.entities.rooms.rooms.room_344.room_344_events import events
from randomizer.entities.rooms.rooms.room_344.room_344_objects import objects

room = Room(
    partition=partition,
    music=M50_NIMBUS_LAND,
    entrance_event=E3624_NIMBUS_SHOP_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
