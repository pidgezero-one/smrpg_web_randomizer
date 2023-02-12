from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_415.room_415_partition import partition
from randomizer.entities.rooms.rooms.room_415.room_415_exits import exits
from randomizer.entities.rooms.rooms.room_415.room_415_events import events

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3737_NIMBUS_CASTLE_BACK_EXIT_LOADER,
    events=events,
    exits=exits,
    objects=[],
    extra_sprite_actions=[
        ExtraSpriteActions.LeanForward,
        ExtraSpriteActions.PraiseFront,
    ]
)
