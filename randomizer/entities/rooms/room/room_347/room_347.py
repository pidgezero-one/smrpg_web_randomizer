"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_347.room_347_partition import partition
from randomizer.entities.rooms.room.room_347.room_347_events import events
from randomizer.entities.rooms.room.room_347.room_347_objects import objects

room = Room(
    partition=partition,
    music=M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
    entrance_event=E2541_BEAN_VALLEY_TOP_PIPE_BASEMENT_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[])
