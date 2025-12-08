"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_443.room_443_partition import partition
from randomizer.entities.rooms.room.room_443.room_443_events import events
from randomizer.entities.rooms.room.room_443.room_443_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E1890_DETERMINE_SIDE_TREASURE_ROOM_TO_LOAD,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[])
