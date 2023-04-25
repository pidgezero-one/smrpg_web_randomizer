"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_90.room_90_partition import partition
from randomizer.entities.rooms.room.room_90.room_90_exits import exits
from randomizer.entities.rooms.room.room_90.room_90_events import events
from randomizer.entities.rooms.room.room_90.room_90_objects import objects

room = Room(
    partition=partition,
    music=M18_ROSE_TOWN,
    entrance_event=E0568_ROSE_ROWN_LIBERATED_WATER_PUMP_HOUSE_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
