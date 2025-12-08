"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_492.room_492_partition import partition
from randomizer.entities.rooms.room.room_492.room_492_events import events
from randomizer.entities.rooms.room.room_492.room_492_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3831_MUSHROOM_KINGDOM_SHOP_CELLAR_MOD,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[])
