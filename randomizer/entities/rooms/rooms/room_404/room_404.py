from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_404.room_404_partition import partition
from randomizer.entities.rooms.rooms.room_404.room_404_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E1786_LANDS_END_SHY_AWAY_WHIRLPOOL_1_SUBROUTINE,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Whirl,
    ],
)
