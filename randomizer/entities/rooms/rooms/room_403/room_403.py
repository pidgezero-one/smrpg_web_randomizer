from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_403.room_403_partition import partition
from randomizer.entities.rooms.rooms.room_403.room_403_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E1785_LANDS_END_FINAL_WHIRLPOOL_1_SUBROUTINE,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Whirl,
    ],
)
