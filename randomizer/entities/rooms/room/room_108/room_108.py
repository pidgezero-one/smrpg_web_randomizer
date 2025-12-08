"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_108.room_108_partition import partition
from randomizer.entities.rooms.room.room_108.room_108_exits import exits
from randomizer.entities.rooms.room.room_108.room_108_events import events
from randomizer.entities.rooms.room.room_108.room_108_objects import objects

room = Room(
    partition=partition,
    music=M33_MOLEVILLE,
    entrance_event=E1649_MOLEVILLE_LIBERATED_EXTERIOR_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SURPRISE_FRAME,
        ExtraSpriteActions.WHIRL,
    ])
