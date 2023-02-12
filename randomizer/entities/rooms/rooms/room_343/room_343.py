from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_343.room_343_partition import partition
from randomizer.entities.rooms.rooms.room_343.room_343_exits import exits
from randomizer.entities.rooms.rooms.room_343.room_343_events import events
from randomizer.entities.rooms.rooms.room_343.room_343_objects import objects

room = Room(
    partition=partition,
    music=M50_NIMBUS_LAND,
    entrance_event=E3616_NIMBUS_INN_LOADER_FROM_DOOR,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Salute,
    ]
)
