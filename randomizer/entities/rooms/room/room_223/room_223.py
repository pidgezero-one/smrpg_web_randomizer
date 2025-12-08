"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_223.room_223_partition import partition
from randomizer.entities.rooms.room.room_223.room_223_events import events
from randomizer.entities.rooms.room.room_223.room_223_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E2363_ABYSS_1ST_BOSS_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SURPRISE_FRAME,
    ])
