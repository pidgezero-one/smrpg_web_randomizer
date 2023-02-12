from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_335.room_335_partition import partition
from randomizer.entities.rooms.rooms.room_335.room_335_events import events
from randomizer.entities.rooms.rooms.room_335.room_335_objects import objects

room = Room(
    partition=partition,
    music=M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
    entrance_event=E2544_BEAN_VALLEY_RIGHTMOST_PIPE_BASEMENT_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
