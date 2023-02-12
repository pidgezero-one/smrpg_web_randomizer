from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_74.room_74_partition import partition
from randomizer.entities.rooms.rooms.room_74.room_74_exits import exits
from randomizer.entities.rooms.rooms.room_74.room_74_events import events
from randomizer.entities.rooms.rooms.room_74.room_74_objects import objects

room = Room(
    partition=partition,
    music=M53_SILENCE,
    entrance_event=E1072_MELODY_BAY_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Swim,
        ExtraSpriteActions.DispleasedFront,
    ]
)
