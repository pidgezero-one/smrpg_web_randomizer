from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_227.room_227_partition import partition
from randomizer.entities.rooms.rooms.room_227.room_227_events import events
from randomizer.entities.rooms.rooms.room_227.room_227_objects import objects

room = Room(
    partition=partition,
    music=M26_FOREST_MAZE,
    entrance_event=E2430_FOREST_PREMAZE_SAVE_ROOM_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DownPipe,
    ],
)
