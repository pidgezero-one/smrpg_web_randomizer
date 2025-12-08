"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_220.room_220_partition import partition
from randomizer.entities.rooms.room.room_220.room_220_exits import exits
from randomizer.entities.rooms.room.room_220.room_220_events import events
from randomizer.entities.rooms.room.room_220.room_220_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E2359_ABYSS_1ST_SAVE_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
