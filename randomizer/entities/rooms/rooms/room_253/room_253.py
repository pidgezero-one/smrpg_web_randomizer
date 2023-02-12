from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_253.room_253_partition import partition
from randomizer.entities.rooms.rooms.room_253.room_253_events import events
from randomizer.entities.rooms.rooms.room_253.room_253_objects import objects

room = Room(
    partition=partition,
    music=M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
    entrance_event=E2478_BEAN_VALLEY_BEANSTALK_ROOM_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Recoil,
        ExtraSpriteActions.DownPipe,
        ExtraSpriteActions.Climb,
    ],
)
