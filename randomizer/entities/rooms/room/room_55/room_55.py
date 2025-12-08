"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_55.room_55_partition import partition
from randomizer.entities.rooms.room.room_55.room_55_exits import exits
from randomizer.entities.rooms.room.room_55.room_55_events import events
from randomizer.entities.rooms.room.room_55.room_55_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E0455_RESUMMON_PIPE_VAULT_ENEMIES,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DOWN_PIPE,
    ])
