from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_336.room_336_partition import partition
from randomizer.entities.rooms.rooms.room_336.room_336_events import events
from randomizer.entities.rooms.rooms.room_336.room_336_objects import objects

room = Room(
    partition=partition,
    music=M33_MOLEVILLE,
    entrance_event=E1856_MOLEVILLE_SHOP_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
