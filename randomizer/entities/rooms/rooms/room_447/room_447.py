from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_447.room_447_partition import partition
from randomizer.entities.rooms.rooms.room_447.room_447_events import events
from randomizer.entities.rooms.rooms.room_447.room_447_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3756_HOT_SPRINGS_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SurpriseFrame,
        ExtraSpriteActions.Mute,
        ExtraSpriteActions.LeanForward,
    ],
)
