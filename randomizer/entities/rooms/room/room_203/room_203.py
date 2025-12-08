"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_203.room_203_partition import partition
from randomizer.entities.rooms.room.room_203.room_203_exits import exits
from randomizer.entities.rooms.room.room_203.room_203_events import events
from randomizer.entities.rooms.room.room_203.room_203_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E1427_MUSHROOM_WAY_1_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
