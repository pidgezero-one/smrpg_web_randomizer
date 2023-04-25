"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_399.room_399_partition import partition
from randomizer.entities.rooms.room.room_399.room_399_exits import exits
from randomizer.entities.rooms.room.room_399.room_399_events import events
from randomizer.entities.rooms.room.room_399.room_399_objects import objects

room = Room(
    partition=partition,
    music=M51_MONSTRO_TOWN,
    entrance_event=E2080_MUSTY_FEARS_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
