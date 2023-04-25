"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_262.room_262_partition import partition
from randomizer.entities.rooms.room.room_262.room_262_events import events
from randomizer.entities.rooms.room.room_262.room_262_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E1795_LANDS_END_UNDERGROUND_LOWER_LEVEL_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
