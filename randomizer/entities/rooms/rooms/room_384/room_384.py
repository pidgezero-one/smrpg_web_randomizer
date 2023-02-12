from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_384.room_384_partition import partition
from randomizer.entities.rooms.rooms.room_384.room_384_exits import exits
from randomizer.entities.rooms.rooms.room_384.room_384_objects import objects

room = Room(
    partition=partition,
    music=M62_BARREL_VOLCANO,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SurpriseFrame,
    ],
)
