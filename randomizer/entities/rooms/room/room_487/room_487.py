"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_487.room_487_partition import partition
from randomizer.entities.rooms.room.room_487.room_487_exits import exits
from randomizer.entities.rooms.room.room_487.room_487_events import events
from randomizer.entities.rooms.room.room_487.room_487_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0261_FADE_MUSIC_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
