from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_376.room_376_partition import partition
from randomizer.entities.rooms.rooms.room_376.room_376_events import events
from randomizer.entities.rooms.rooms.room_376.room_376_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E2180_KEEP_CHEWY_BATTLE_ROOM_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
