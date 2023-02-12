from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_123.room_123_partition import partition
from randomizer.entities.rooms.rooms.room_123.room_123_events import events
from randomizer.entities.rooms.rooms.room_123.room_123_objects import objects

room = Room(
    partition=partition,
    music=M07_PIPE_VAULT,
    entrance_event=E0435_PIPE_VAULT_ROOM_1_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
