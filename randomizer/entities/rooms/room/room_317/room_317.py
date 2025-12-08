"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_317.room_317_partition import partition
from randomizer.entities.rooms.room.room_317.room_317_exits import exits
from randomizer.entities.rooms.room.room_317.room_317_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E1782_LANDS_END_DESERT_1_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.WHIRL,
    ])
