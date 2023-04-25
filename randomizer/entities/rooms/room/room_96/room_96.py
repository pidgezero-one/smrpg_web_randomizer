"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_96.room_96_partition import partition
from randomizer.entities.rooms.room.room_96.room_96_exits import exits
from randomizer.entities.rooms.room.room_96.room_96_events import events
from randomizer.entities.rooms.room.room_96.room_96_objects import objects

room = Room(
    partition=partition,
    music=M18_ROSE_TOWN,
    entrance_event=E0561_PLACE_LINK_IN_ROSE_TOWN,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SLEEP,
    ],
)
