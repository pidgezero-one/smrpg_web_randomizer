from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_326.room_326_partition import partition
from randomizer.entities.rooms.rooms.room_326.room_326_events import events
from randomizer.entities.rooms.rooms.room_326.room_326_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0368_MUSHROOM_KINGDOM_OCCUPIED_THRONE_ROOM_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
