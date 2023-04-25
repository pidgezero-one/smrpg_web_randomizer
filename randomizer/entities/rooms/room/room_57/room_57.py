"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_57.room_57_partition import partition
from randomizer.entities.rooms.room.room_57.room_57_exits import exits
from randomizer.entities.rooms.room.room_57.room_57_events import events
from randomizer.entities.rooms.room.room_57.room_57_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E3135_SEWERS_GENERIC_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DOWN_PIPE,
        ExtraSpriteActions.SWIM,
    ],
)
