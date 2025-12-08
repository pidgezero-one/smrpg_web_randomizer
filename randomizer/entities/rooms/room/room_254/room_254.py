"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_254.room_254_partition import partition
from randomizer.entities.rooms.room.room_254.room_254_exits import exits
from randomizer.entities.rooms.room.room_254.room_254_events import events
from randomizer.entities.rooms.room.room_254.room_254_objects import objects

room = Room(
    partition=partition,
    music=M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
    entrance_event=E2555_BEAN_VALLEY_BOSS_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DOWN_PIPE,
    ])
