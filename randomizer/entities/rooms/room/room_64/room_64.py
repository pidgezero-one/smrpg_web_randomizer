"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_64.room_64_partition import partition
from randomizer.entities.rooms.room.room_64.room_64_exits import exits
from randomizer.entities.rooms.room.room_64.room_64_events import events
from randomizer.entities.rooms.room.room_64.room_64_objects import objects

room = Room(
    partition=partition,
    music=M39_MARRYMORE,
    entrance_event=E0670_MARRYMORE_UNOCCUPIED_EXTERIOR_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
