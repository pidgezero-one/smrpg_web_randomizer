"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_153.room_153_partition import partition
from randomizer.entities.rooms.room.room_153.room_153_events import events
from randomizer.entities.rooms.room.room_153.room_153_objects import objects

room = Room(
    partition=partition,
    music=M39_MARRYMORE,
    entrance_event=E0729_SEVERAL_MARRYMORE_ROOM_LOADERS,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[])
