from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_459.room_459_partition import partition
from randomizer.entities.rooms.rooms.room_459.room_459_events import events
from randomizer.entities.rooms.rooms.room_459.room_459_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E2160_KEEP_TERRA_COTTA_BATTLE_ROOM_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
