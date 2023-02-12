from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_337.room_337_partition import partition
from randomizer.entities.rooms.rooms.room_337.room_337_events import events
from randomizer.entities.rooms.rooms.room_337.room_337_objects import objects

room = Room(
    partition=partition,
    music=M33_MOLEVILLE,
    entrance_event=E1616_MOLEVILLE_INN_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Salute,
        ExtraSpriteActions.Sleep,
    ],
)
