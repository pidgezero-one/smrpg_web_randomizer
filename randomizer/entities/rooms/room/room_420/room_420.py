"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_420.room_420_partition import partition
from randomizer.entities.rooms.room.room_420.room_420_exits import exits
from randomizer.entities.rooms.room.room_420.room_420_events import events
from randomizer.entities.rooms.room.room_420.room_420_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E1688_TEMPLE_FORTUNE_HEADS_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
