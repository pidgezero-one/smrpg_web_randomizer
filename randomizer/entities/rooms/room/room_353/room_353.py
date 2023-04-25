"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_353.room_353_partition import partition
from randomizer.entities.rooms.room.room_353.room_353_exits import exits
from randomizer.entities.rooms.room.room_353.room_353_events import events
from randomizer.entities.rooms.room.room_353.room_353_objects import objects

room = Room(
    partition=partition,
    music=M07_PIPE_VAULT,
    entrance_event=E2096_HINO_MART_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
