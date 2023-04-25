"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_128.room_128_partition import partition
from randomizer.entities.rooms.room.room_128.room_128_events import events
from randomizer.entities.rooms.room.room_128.room_128_objects import objects

room = Room(
    partition=partition,
    music=M07_PIPE_VAULT,
    entrance_event=E0443_PIPE_VAULT_CHOMPWEED_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
