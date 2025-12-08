"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_130.room_130_partition import partition
from randomizer.entities.rooms.room.room_130.room_130_exits import exits
from randomizer.entities.rooms.room.room_130.room_130_events import events
from randomizer.entities.rooms.room.room_130.room_130_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
