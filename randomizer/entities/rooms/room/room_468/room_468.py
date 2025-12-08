"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_468.room_468_partition import partition
from randomizer.entities.rooms.room.room_468.room_468_events import events
from randomizer.entities.rooms.room.room_468.room_468_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E3778_BALL_SOLITAIRE_SET_PUZZLE,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.MUTE,
    ])
