"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_85.room_85_partition import partition
from randomizer.entities.rooms.room.room_85.room_85_events import events
from randomizer.entities.rooms.room.room_85.room_85_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0512_ROSE_TOWN_OCCUPIED_INN_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DOWN_PIPE,
    ])
