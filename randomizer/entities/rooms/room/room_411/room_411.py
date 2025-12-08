"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_411.room_411_partition import partition
from randomizer.entities.rooms.room.room_411.room_411_exits import exits
from randomizer.entities.rooms.room.room_411.room_411_events import events
from randomizer.entities.rooms.room.room_411.room_411_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3927_NIMBUS_CASTLE_EXIT_HALLWAY_SAVE_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
