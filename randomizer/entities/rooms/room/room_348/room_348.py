"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_348.room_348_partition import partition
from randomizer.entities.rooms.room.room_348.room_348_objects import objects

room = Room(
    partition=partition,
    music=M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
    entrance_event=E2543_BEAN_VALLEY_BOTTOM_LEFT_PIPE_BASEMENT_LOADER,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
