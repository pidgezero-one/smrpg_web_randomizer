"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_117.room_117_partition import partition
from randomizer.entities.rooms.room.room_117.room_117_exits import exits
from randomizer.entities.rooms.room.room_117.room_117_events import events
from randomizer.entities.rooms.room.room_117.room_117_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3714_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
