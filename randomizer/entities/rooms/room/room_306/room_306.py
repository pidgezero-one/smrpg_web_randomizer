"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_306.room_306_partition import partition
from randomizer.entities.rooms.room.room_306.room_306_exits import exits
from randomizer.entities.rooms.room.room_306.room_306_events import events

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=[],
    extra_sprite_actions=[
        ExtraSpriteActions.SLEEP,
    ],
)
