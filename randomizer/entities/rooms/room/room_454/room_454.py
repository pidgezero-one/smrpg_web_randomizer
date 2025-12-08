"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_454.room_454_partition import partition
from randomizer.entities.rooms.room.room_454.room_454_events import events
from randomizer.entities.rooms.room.room_454.room_454_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3376_KEEP_6_DOOR_LOBBY_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.FLOP,
    ])
