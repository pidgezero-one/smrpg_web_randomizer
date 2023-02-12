from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_95.room_95_partition import partition
from randomizer.entities.rooms.rooms.room_95.room_95_exits import exits
from randomizer.entities.rooms.rooms.room_95.room_95_events import events
from randomizer.entities.rooms.rooms.room_95.room_95_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0531_ROSE_TOWN_OCCUPIED_INN_2F_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Sleep,
    ]
)
