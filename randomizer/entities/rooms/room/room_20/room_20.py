"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_20.room_20_partition import partition
from randomizer.entities.rooms.room.room_20.room_20_exits import exits
from randomizer.entities.rooms.room.room_20.room_20_events import events
from randomizer.entities.rooms.room.room_20.room_20_objects import objects

room = Room(
    partition=partition,
    music=M02_MUSHROOM_KINGDOM,
    entrance_event=E0347_TOADSTOOLS_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
