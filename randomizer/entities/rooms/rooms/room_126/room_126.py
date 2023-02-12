from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_126.room_126_partition import partition
from randomizer.entities.rooms.rooms.room_126.room_126_events import events
from randomizer.entities.rooms.rooms.room_126.room_126_objects import objects

room = Room(
    partition=partition,
    music=M07_PIPE_VAULT,
    entrance_event=E0434_PIPE_VAULT_RED_ROOM_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
