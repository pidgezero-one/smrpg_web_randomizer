from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_83.room_83_partition import partition
from randomizer.entities.rooms.rooms.room_83.room_83_exits import exits
from randomizer.entities.rooms.rooms.room_83.room_83_events import events
from randomizer.entities.rooms.rooms.room_83.room_83_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0529_ROSE_TOWN_OCCUPIED_EXTERIOR_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DownPipe,
    ]
)
