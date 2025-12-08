"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_440.room_440_partition import partition
from randomizer.entities.rooms.room.room_440.room_440_exits import exits
from randomizer.entities.rooms.room.room_440.room_440_events import events
from randomizer.entities.rooms.room.room_440.room_440_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3740_NIMBUS_CASTLE_LIBERATED_THRONE_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
