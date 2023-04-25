"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_461.room_461_partition import partition
from randomizer.entities.rooms.room.room_461.room_461_events import events
from randomizer.entities.rooms.room.room_461.room_461_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E2170_KEEP_BOBOMB_BATTLE_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
