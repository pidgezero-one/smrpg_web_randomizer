from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_27.room_27_partition import partition
from randomizer.entities.rooms.rooms.room_27.room_27_exits import exits
from randomizer.entities.rooms.rooms.room_27.room_27_events import events
from randomizer.entities.rooms.rooms.room_27.room_27_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Swim,
        ExtraSpriteActions.Whirl,
    ]
)
