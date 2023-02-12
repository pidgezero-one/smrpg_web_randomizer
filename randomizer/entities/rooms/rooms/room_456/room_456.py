from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_456.room_456_partition import partition
from randomizer.entities.rooms.rooms.room_456.room_456_events import events
from randomizer.entities.rooms.rooms.room_456.room_456_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E1836_KEEP_DONKEY_ROOM_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.TumbleBack,
        ExtraSpriteActions.Recoil,
    ],
)
