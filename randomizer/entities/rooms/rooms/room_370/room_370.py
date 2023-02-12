from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_370.room_370_partition import partition
from randomizer.entities.rooms.rooms.room_370.room_370_events import events
from randomizer.entities.rooms.rooms.room_370.room_370_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3753_HOT_SPRINGS_LOBBY_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SurpriseFrame,
    ],
)
