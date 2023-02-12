from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_12.room_12_partition import partition
from randomizer.entities.rooms.rooms.room_12.room_12_exits import exits
from randomizer.entities.rooms.rooms.room_12.room_12_events import events
from randomizer.entities.rooms.rooms.room_12.room_12_objects import objects

room = Room(
    partition=partition,
    music=M39_MARRYMORE,
    entrance_event=E0613_MARRYMORE_SUITE_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DownPipe,
        ExtraSpriteActions.Sleep,
    ]
)
