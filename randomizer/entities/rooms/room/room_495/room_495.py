"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_495.room_495_partition import partition
from randomizer.entities.rooms.room.room_495.room_495_exits import exits
from randomizer.entities.rooms.room.room_495.room_495_events import events
from randomizer.entities.rooms.room.room_495.room_495_objects import objects

room = Room(
    partition=partition,
    music=M02_MUSHROOM_KINGDOM,
    entrance_event=E0261_FADE_MUSIC_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
