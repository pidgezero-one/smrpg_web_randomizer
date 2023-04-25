"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_125.room_125_partition import partition
from randomizer.entities.rooms.room.room_125.room_125_events import events
from randomizer.entities.rooms.room.room_125.room_125_objects import objects

room = Room(
    partition=partition,
    music=M07_PIPE_VAULT,
    entrance_event=E3604_PIPE_VAULT_TRIPLE_CHEST_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DEFEND,
    ],
)
