from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_159.room_159_partition import partition
from randomizer.entities.rooms.rooms.room_159.room_159_events import events
from randomizer.entities.rooms.rooms.room_159.room_159_objects import objects

room = Room(
    partition=partition,
    music=M34_STAR_HILL,
    entrance_event=E2405_STAR_HILL_FINAL_AREA_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
