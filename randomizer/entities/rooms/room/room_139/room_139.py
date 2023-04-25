"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_139.room_139_partition import partition
from randomizer.entities.rooms.room.room_139.room_139_exits import exits
from randomizer.entities.rooms.room.room_139.room_139_events import events
from randomizer.entities.rooms.room.room_139.room_139_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E1561_LANDS_END_GECKIT_CANNON_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
