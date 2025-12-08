"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_319.room_319_partition import partition
from randomizer.entities.rooms.room.room_319.room_319_exits import exits
from randomizer.entities.rooms.room.room_319.room_319_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E1783_LANDS_END_FINAL_WHIRLPOOL_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.WHIRL,
    ])
