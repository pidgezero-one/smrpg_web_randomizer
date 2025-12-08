"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_33.room_33_partition import partition
from randomizer.entities.rooms.room.room_33.room_33_exits import exits
from randomizer.entities.rooms.room.room_33.room_33_events import events
from randomizer.entities.rooms.room.room_33.room_33_objects import objects

room = Room(
    partition=partition,
    music=M04_YOSTER_ISLAND,
    entrance_event=E0455_RESUMMON_PIPE_VAULT_ENEMIES,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DOWN_PIPE,
    ])
