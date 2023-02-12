from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_493.room_493_partition import partition
from randomizer.entities.rooms.rooms.room_493.room_493_exits import exits
from randomizer.entities.rooms.rooms.room_493.room_493_events import events
from randomizer.entities.rooms.rooms.room_493.room_493_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0265_OCCUPIED_MK_INN_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DownPipe,
    ]
)
