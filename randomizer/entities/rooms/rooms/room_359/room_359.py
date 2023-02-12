from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_359.room_359_partition import partition
from randomizer.entities.rooms.rooms.room_359.room_359_exits import exits
from randomizer.entities.rooms.rooms.room_359.room_359_objects import objects

room = Room(
    partition=partition,
    music=M62_BARREL_VOLCANO,
    entrance_event=E3328_VOLCANO_GENERIC_LOADER_1,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SurpriseFrame,
    ],
)
