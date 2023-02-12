from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_209.room_209_partition import partition
from randomizer.entities.rooms.rooms.room_209.room_209_exits import exits
from randomizer.entities.rooms.rooms.room_209.room_209_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E1121_SEASIDE_OCCUPIED_INN_1F_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Salute,
    ],
)
