"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_340.room_340_partition import partition
from randomizer.entities.rooms.room.room_340.room_340_events import events
from randomizer.entities.rooms.room.room_340.room_340_objects import objects

room = Room(
    partition=partition,
    music=M33_MOLEVILLE,
    entrance_event=E1614_MOLEVILLE_SWAP_SHOP_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
