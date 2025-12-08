"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_253.room_253_partition import partition
from randomizer.entities.rooms.room.room_253.room_253_events import events
from randomizer.entities.rooms.room.room_253.room_253_objects import objects

room = Room(
    partition=partition,
    music=M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
    entrance_event=E2478_BEAN_VALLEY_BEANSTALK_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.RECOIL,
        ExtraSpriteActions.DOWN_PIPE,
        ExtraSpriteActions.CLIMB,
    ])
