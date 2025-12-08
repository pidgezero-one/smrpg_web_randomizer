"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_491.room_491_partition import partition
from randomizer.entities.rooms.room.room_491.room_491_exits import exits
from randomizer.entities.rooms.room.room_491.room_491_events import events
from randomizer.entities.rooms.room.room_491.room_491_objects import objects

room = Room(
    partition=partition,
    music=M02_MUSHROOM_KINGDOM,
    entrance_event=E0261_FADE_MUSIC_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
