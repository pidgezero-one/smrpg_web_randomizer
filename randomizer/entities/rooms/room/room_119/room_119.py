"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_119.room_119_partition import partition
from randomizer.entities.rooms.room.room_119.room_119_exits import exits
from randomizer.entities.rooms.room.room_119.room_119_events import events
from randomizer.entities.rooms.room.room_119.room_119_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3701_NIMBUS_CASTLE_LEFT_SHAMAN_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
