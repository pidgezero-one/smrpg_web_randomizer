from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_68.room_68_partition import partition
from randomizer.entities.rooms.rooms.room_68.room_68_events import events
from randomizer.entities.rooms.rooms.room_68.room_68_objects import objects

room = Room(
    partition=partition,
    music=M22_MIDAS_RIVER,
    entrance_event=E1568_MIDAS_RIVER_BEGIN_BARREL_SECTION,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.TumbleFront,
        ExtraSpriteActions.Wobble,
    ],
)
