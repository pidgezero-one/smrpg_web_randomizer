from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_338.room_338_partition import partition
from randomizer.entities.rooms.rooms.room_338.room_338_exits import exits
from randomizer.entities.rooms.rooms.room_338.room_338_events import events
from randomizer.entities.rooms.rooms.room_338.room_338_objects import objects

room = Room(
    partition=partition,
    music=M33_MOLEVILLE,
    entrance_event=E1627_DYNA_HOUSE_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SurpriseFrame,
    ]
)
