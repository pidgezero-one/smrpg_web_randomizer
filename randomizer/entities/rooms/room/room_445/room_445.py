"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_445.room_445_partition import partition
from randomizer.entities.rooms.room.room_445.room_445_events import events
from randomizer.entities.rooms.room.room_445.room_445_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E1889_ABYSS_SIDE_TREASURE_ROOMS_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[])
