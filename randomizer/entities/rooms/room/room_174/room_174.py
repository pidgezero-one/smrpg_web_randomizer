"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_174.room_174_partition import partition
from randomizer.entities.rooms.room.room_174.room_174_exits import exits
from randomizer.entities.rooms.room.room_174.room_174_events import events
from randomizer.entities.rooms.room.room_174.room_174_objects import objects

room = Room(
    partition=partition,
    music=M44_SEA,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.WHIRL,
        ExtraSpriteActions.SWIM,
    ])
