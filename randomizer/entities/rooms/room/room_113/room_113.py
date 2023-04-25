"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_113.room_113_partition import partition
from randomizer.entities.rooms.room.room_113.room_113_exits import exits
from randomizer.entities.rooms.room.room_113.room_113_events import events
from randomizer.entities.rooms.room.room_113.room_113_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0828_NIMBUS_CASTLE_SINGLE_BIRD_STATUE_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
