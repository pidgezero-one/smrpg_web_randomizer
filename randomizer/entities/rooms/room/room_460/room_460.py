"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_460.room_460_partition import partition
from randomizer.entities.rooms.room.room_460.room_460_events import events
from randomizer.entities.rooms.room.room_460.room_460_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E2165_KEEP_ALLEY_RAT_BATTLE_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[])
