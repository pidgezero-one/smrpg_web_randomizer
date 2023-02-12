from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_154.room_154_partition import partition
from randomizer.entities.rooms.rooms.room_154.room_154_events import events
from randomizer.entities.rooms.rooms.room_154.room_154_objects import objects

room = Room(
    partition=partition,
    music=M39_MARRYMORE,
    entrance_event=E0600_MARRYMORE_OCCUPIED_CHAPEL_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
