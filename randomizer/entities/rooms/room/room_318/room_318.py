"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_318.room_318_partition import partition
from randomizer.entities.rooms.room.room_318.room_318_exits import exits
from randomizer.entities.rooms.room.room_318.room_318_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E1787_LANDS_END_DESERT_1_RIGHT_WHIRLPOOL_SUBROUTINE,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.WHIRL,
    ])
