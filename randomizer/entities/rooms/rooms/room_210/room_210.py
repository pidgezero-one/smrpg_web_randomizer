from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_210.room_210_partition import partition
from randomizer.entities.rooms.rooms.room_210.room_210_exits import exits
from randomizer.entities.rooms.rooms.room_210.room_210_events import events
from randomizer.entities.rooms.rooms.room_210.room_210_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E1122_SEASIDE_OCCUPIED_INN_2F_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Sleep,
    ]
)
