from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_91.room_91_partition import partition
from randomizer.entities.rooms.rooms.room_91.room_91_events import events
from randomizer.entities.rooms.rooms.room_91.room_91_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0563_SUMMONS_HUSBAND_IN_ROSE_TOWN_COUPLES_HOUSE,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
