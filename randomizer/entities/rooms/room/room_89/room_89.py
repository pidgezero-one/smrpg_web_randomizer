"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_89.room_89_partition import partition
from randomizer.entities.rooms.room.room_89.room_89_exits import exits
from randomizer.entities.rooms.room.room_89.room_89_events import events
from randomizer.entities.rooms.room.room_89.room_89_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0552_ROSE_TOWN_OCCUPIED_INTRO_TOAD_MOVEMENT,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
