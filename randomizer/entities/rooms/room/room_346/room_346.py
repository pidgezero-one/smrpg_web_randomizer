"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_346.room_346_partition import partition
from randomizer.entities.rooms.room.room_346.room_346_exits import exits
from randomizer.entities.rooms.room.room_346.room_346_objects import objects

room = Room(
    partition=partition,
    music=M50_NIMBUS_LAND,
    entrance_event=E3617_NIMBUS_INN_BEDROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SLEEP,
    ],
)
