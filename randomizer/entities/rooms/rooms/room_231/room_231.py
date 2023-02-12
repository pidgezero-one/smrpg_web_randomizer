from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_231.room_231_partition import partition
from randomizer.entities.rooms.rooms.room_231.room_231_events import events

room = Room(
    partition=partition,
    music=M26_FOREST_MAZE,
    entrance_event=E2598_FOREST_SECRET_ENTRANCE_LOADER,
    events=events,
    exit_fields=[],
    objects=[],
    extra_sprite_actions=[
        ExtraSpriteActions.DownPipe,
    ],
)
