"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_120.room_120_partition import partition
from randomizer.entities.rooms.room.room_120.room_120_exits import exits
from randomizer.entities.rooms.room.room_120.room_120_events import events
from randomizer.entities.rooms.room.room_120.room_120_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3729_NIMBUS_CASTLE_OCCUPIED_THRONE_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
