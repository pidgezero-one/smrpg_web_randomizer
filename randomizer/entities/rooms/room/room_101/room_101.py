"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_101.room_101_partition import partition
from randomizer.entities.rooms.room.room_101.room_101_exits import exits
from randomizer.entities.rooms.room.room_101.room_101_events import events
from randomizer.entities.rooms.room.room_101.room_101_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E3919_BOOSTER_PASS_BACK_ENTRANCE_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.FLOP,
    ],
)
