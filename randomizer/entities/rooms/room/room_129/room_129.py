"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_129.room_129_partition import partition
from randomizer.entities.rooms.room.room_129.room_129_events import events
from randomizer.entities.rooms.room.room_129.room_129_objects import objects

room = Room(
    partition=partition,
    music=M07_PIPE_VAULT,
    entrance_event=E0467_PIPE_VAULT_PLATFORMING_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[])
