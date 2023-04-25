"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_124.room_124_partition import partition
from randomizer.entities.rooms.room.room_124.room_124_events import events
from randomizer.entities.rooms.room.room_124.room_124_objects import objects

room = Room(
    partition=partition,
    music=M07_PIPE_VAULT,
    entrance_event=E0269_PIPE_UP_SUBROUTINE,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
