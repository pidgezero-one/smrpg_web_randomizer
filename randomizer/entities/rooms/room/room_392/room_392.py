"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_392.room_392_partition import partition
from randomizer.entities.rooms.room.room_392.room_392_exits import exits
from randomizer.entities.rooms.room.room_392.room_392_events import events
from randomizer.entities.rooms.room.room_392.room_392_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0841_VOLCANO_FINAL_PRE_EXIT_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
