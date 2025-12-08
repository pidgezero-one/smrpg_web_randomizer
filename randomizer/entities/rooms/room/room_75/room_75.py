"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_75.room_75_partition import partition
from randomizer.entities.rooms.room.room_75.room_75_exits import exits
from randomizer.entities.rooms.room.room_75.room_75_events import events
from randomizer.entities.rooms.room.room_75.room_75_objects import objects

room = Room(
    partition=partition,
    music=M17_TADPOLE_POND,
    entrance_event=E1104_TADPOLE_POND_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
