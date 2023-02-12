from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_470.room_470_partition import partition
from randomizer.entities.rooms.rooms.room_470.room_470_exits import exits
from randomizer.entities.rooms.rooms.room_470.room_470_events import events
from randomizer.entities.rooms.rooms.room_470.room_470_objects import objects

room = Room(
    partition=partition,
    music=M56_FACTORY,
    entrance_event=E2601_FACTORY_4TH_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.LeanBack,
        ExtraSpriteActions.LeanBack2,
        ExtraSpriteActions.LeanBack,
        ExtraSpriteActions.ClimbFrame,
    ]
)
