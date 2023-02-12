from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_105.room_105_partition import partition
from randomizer.entities.rooms.rooms.room_105.room_105_exits import exits
from randomizer.entities.rooms.rooms.room_105.room_105_events import events
from randomizer.entities.rooms.rooms.room_105.room_105_objects import objects

room = Room(
    partition=partition,
    music=M33_MOLEVILLE,
    entrance_event=E1627_DYNA_HOUSE_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Whirl,
    ]
)
