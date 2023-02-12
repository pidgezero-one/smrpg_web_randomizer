from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_465.room_465_partition import partition
from randomizer.entities.rooms.rooms.room_465.room_465_events import events
from randomizer.entities.rooms.rooms.room_465.room_465_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E3357_KEEP_BUTTON_GAME_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Mute,
    ],
)
