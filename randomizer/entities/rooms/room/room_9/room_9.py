"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_9.room_9_partition import partition
from randomizer.entities.rooms.room.room_9.room_9_exits import exits
from randomizer.entities.rooms.room.room_9.room_9_events import events
from randomizer.entities.rooms.room.room_9.room_9_objects import objects

room = Room(
    partition=partition,
    music=M39_MARRYMORE,
    entrance_event=E0935_MARRYMORE_INN_REGULAR_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SLEEP,
    ],
)
