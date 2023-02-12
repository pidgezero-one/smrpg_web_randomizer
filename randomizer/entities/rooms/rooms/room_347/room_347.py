from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_347.room_347_partition import partition
from randomizer.entities.rooms.rooms.room_347.room_347_events import events
from randomizer.entities.rooms.rooms.room_347.room_347_objects import objects

room = Room(
    partition=partition,
    music=M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
    entrance_event=E2541_BEAN_VALLEY_TOP_PIPE_BASEMENT_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
