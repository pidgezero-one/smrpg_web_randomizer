"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_404.room_404_partition import partition
from randomizer.entities.rooms.room.room_404.room_404_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E1786_LANDS_END_SHY_AWAY_WHIRLPOOL_1_SUBROUTINE,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.WHIRL,
    ],
)
