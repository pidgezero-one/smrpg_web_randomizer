from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_408.room_408_partition import partition
from randomizer.entities.rooms.rooms.room_408.room_408_events import events
from randomizer.entities.rooms.rooms.room_408.room_408_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3702_NIMBUS_CASTLE_RIGHT_SHAMAN_ROOM_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
