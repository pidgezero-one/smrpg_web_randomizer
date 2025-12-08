"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_109.room_109_partition import partition
from randomizer.entities.rooms.room.room_109.room_109_exits import exits
from randomizer.entities.rooms.room.room_109.room_109_events import events
from randomizer.entities.rooms.room.room_109.room_109_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3670_NIMBUS_CASTLE_MAIN_HALL_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
