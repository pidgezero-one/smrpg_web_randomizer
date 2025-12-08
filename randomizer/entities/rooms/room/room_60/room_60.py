"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_60.room_60_partition import partition
from randomizer.entities.rooms.room.room_60.room_60_events import events
from randomizer.entities.rooms.room.room_60.room_60_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E3135_SEWERS_GENERIC_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DOWN_PIPE,
    ])
