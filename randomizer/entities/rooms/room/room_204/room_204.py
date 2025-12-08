"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_204.room_204_partition import partition
from randomizer.entities.rooms.room.room_204.room_204_exits import exits
from randomizer.entities.rooms.room.room_204.room_204_events import events
from randomizer.entities.rooms.room.room_204.room_204_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E1423_MUSHROOM_WAY_2_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
