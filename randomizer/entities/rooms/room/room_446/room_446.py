"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_446.room_446_partition import partition
from randomizer.entities.rooms.room.room_446.room_446_events import events
from randomizer.entities.rooms.room.room_446.room_446_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[])
