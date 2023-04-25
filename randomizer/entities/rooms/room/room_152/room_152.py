"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_152.room_152_partition import partition
from randomizer.entities.rooms.room.room_152.room_152_exits import exits
from randomizer.entities.rooms.room.room_152.room_152_events import events

room = Room(
    partition=partition,
    music=M39_MARRYMORE,
    entrance_event=E0729_SEVERAL_MARRYMORE_ROOM_LOADERS,
    events=events,
    exits=exits,
    objects=[],
    extra_sprite_actions=[],
)
