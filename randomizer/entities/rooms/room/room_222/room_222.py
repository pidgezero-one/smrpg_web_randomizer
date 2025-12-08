"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_222.room_222_partition import partition
from randomizer.entities.rooms.room.room_222.room_222_exits import exits
from randomizer.entities.rooms.room.room_222.room_222_events import events
from randomizer.entities.rooms.room.room_222.room_222_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E2362_ABYSS_FOUR_BOLT_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
