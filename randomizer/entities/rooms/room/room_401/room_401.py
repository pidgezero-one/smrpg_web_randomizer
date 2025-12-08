"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_401.room_401_partition import partition
from randomizer.entities.rooms.room.room_401.room_401_exits import exits
from randomizer.entities.rooms.room.room_401.room_401_events import events
from randomizer.entities.rooms.room.room_401.room_401_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E1590_SEWER_PIPE_TO_LANDS_END_SUBROUTINE,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
