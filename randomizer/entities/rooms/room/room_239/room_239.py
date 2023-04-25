"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_239.room_239_partition import partition
from randomizer.entities.rooms.room.room_239.room_239_exits import exits
from randomizer.entities.rooms.room.room_239.room_239_events import events
from randomizer.entities.rooms.room.room_239.room_239_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E2409_ABYSS_ROOM_BEFORE_1ST_BOSS_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
