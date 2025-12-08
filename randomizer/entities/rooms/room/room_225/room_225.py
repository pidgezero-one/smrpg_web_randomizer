"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_225.room_225_partition import partition
from randomizer.entities.rooms.room.room_225.room_225_exits import exits
from randomizer.entities.rooms.room.room_225.room_225_events import events
from randomizer.entities.rooms.room.room_225.room_225_objects import objects

room = Room(
    partition=partition,
    music=M26_FOREST_MAZE,
    entrance_event=E1552_FOREST_TREE_TRUNK_AREA_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DOWN_PIPE,
    ])
