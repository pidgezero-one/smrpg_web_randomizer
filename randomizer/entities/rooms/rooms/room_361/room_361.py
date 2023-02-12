from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_361.room_361_partition import partition
from randomizer.entities.rooms.rooms.room_361.room_361_exits import exits
from randomizer.entities.rooms.rooms.room_361.room_361_objects import objects

room = Room(
    partition=partition,
    music=M62_BARREL_VOLCANO,
    entrance_event=E3333_VOLCANO_GENERIC_LOADER_2,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SurpriseFrame,
    ],
)
