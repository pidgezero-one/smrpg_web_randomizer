"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_377.room_377_partition import partition
from randomizer.entities.rooms.room.room_377.room_377_events import events
from randomizer.entities.rooms.room.room_377.room_377_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E2185_KEEP_SPARKY_BATTLE_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[])
