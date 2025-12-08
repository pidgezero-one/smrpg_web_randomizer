"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_418.room_418_partition import partition
from randomizer.entities.rooms.room.room_418.room_418_exits import exits
from randomizer.entities.rooms.room.room_418.room_418_events import events
from randomizer.entities.rooms.room.room_418.room_418_objects import objects

room = Room(
    partition=partition,
    music=M18_ROSE_TOWN,
    entrance_event=E2384_GARDENERS_HOUSE_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.FLOP,
        ExtraSpriteActions.DIZZY,
        ExtraSpriteActions.CLIMB,
    ])
