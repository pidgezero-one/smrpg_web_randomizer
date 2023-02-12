from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_157.room_157_partition import partition
from randomizer.entities.rooms.rooms.room_157.room_157_events import events
from randomizer.entities.rooms.rooms.room_157.room_157_objects import objects

room = Room(
    partition=partition,
    music=M34_STAR_HILL,
    entrance_event=E2524_STAR_HILL_2ND_ROOM_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
