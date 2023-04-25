"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_286.room_286_partition import partition
from randomizer.entities.rooms.room.room_286.room_286_exits import exits
from randomizer.entities.rooms.room.room_286.room_286_events import events
from randomizer.entities.rooms.room.room_286.room_286_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.TUMBLE_FRONT,
        ExtraSpriteActions.SURPRISE_FRAME,
    ],
)
