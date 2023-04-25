"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_402.room_402_partition import partition
from randomizer.entities.rooms.room.room_402.room_402_exits import exits
from randomizer.entities.rooms.room.room_402.room_402_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E1784_LANDS_END_DESERT_1_LEFT_WHIRLPOOL_SUBROUTINE,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.WHIRL,
    ],
)
