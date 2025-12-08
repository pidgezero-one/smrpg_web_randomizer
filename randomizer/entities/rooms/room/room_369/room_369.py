"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_369.room_369_partition import partition
from randomizer.entities.rooms.room.room_369.room_369_events import events
from randomizer.entities.rooms.room.room_369.room_369_objects import objects

room = Room(
    partition=partition,
    music=M50_NIMBUS_LAND,
    entrance_event=E3761_NIMBUS_MEZZANINE_LOADER,
    events=events,
    exits=[],
    objects=objects,
    extra_sprite_actions=[])
