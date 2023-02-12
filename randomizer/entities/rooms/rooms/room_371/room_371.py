from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_371.room_371_partition import partition
from randomizer.entities.rooms.rooms.room_371.room_371_events import events
from randomizer.entities.rooms.rooms.room_371.room_371_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.PraiseFront,
    ],
)
