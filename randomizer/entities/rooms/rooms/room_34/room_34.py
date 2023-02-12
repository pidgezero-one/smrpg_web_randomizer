from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_34.room_34_partition import partition
from randomizer.entities.rooms.rooms.room_34.room_34_exits import exits
from randomizer.entities.rooms.rooms.room_34.room_34_events import events
from randomizer.entities.rooms.rooms.room_34.room_34_objects import objects

room = Room(
    partition=partition,
    music=M04_YOSTER_ISLAND,
    entrance_event=E3824_YOSTER_ISLE_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Yoshi,
    ]
)
