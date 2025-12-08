"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_127.room_127_partition import partition
from randomizer.entities.rooms.room.room_127.room_127_events import events
from randomizer.entities.rooms.room.room_127.room_127_objects import objects

room = Room(
    partition=partition,
    music=M07_PIPE_VAULT,
    entrance_event=E0428_PIPE_VAULT_THWOMP_ROOM_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.FLOP,
        ExtraSpriteActions.TUMBLE_BACK,
    ])
