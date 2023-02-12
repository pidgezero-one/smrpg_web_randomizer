from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_7.room_7_partition import partition
from randomizer.entities.rooms.rooms.room_7.room_7_events import events
from randomizer.entities.rooms.rooms.room_7.room_7_objects import objects

room = Room(
    partition=partition,
    music=M39_MARRYMORE,
    entrance_event=E0611_MARRYMORE_INN_LOBBY_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
