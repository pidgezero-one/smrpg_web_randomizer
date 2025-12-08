"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_333.room_333_partition import partition
from randomizer.entities.rooms.room.room_333.room_333_exits import exits
from randomizer.entities.rooms.room.room_333.room_333_events import events

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E3135_SEWERS_GENERIC_LOADER,
    events=events,
    exits=exits,
    objects=[],
    extra_sprite_actions=[
        ExtraSpriteActions.DOWN_PIPE,
    ])
