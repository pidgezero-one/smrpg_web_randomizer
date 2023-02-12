from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_70.room_70_partition import partition
from randomizer.entities.rooms.rooms.room_70.room_70_objects import objects

room = Room(
    partition=partition,
    music=M22_MIDAS_RIVER,
    entrance_event=E3482_MIDAS_RIVER_TOP_TUNNEL_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Swim,
    ],
)
