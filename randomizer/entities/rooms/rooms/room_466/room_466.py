from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_466.room_466_partition import partition
from randomizer.entities.rooms.rooms.room_466.room_466_events import events
from randomizer.entities.rooms.rooms.room_466.room_466_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E3364_KEEP_LOGIC_GAME_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Mute,
    ],
)
