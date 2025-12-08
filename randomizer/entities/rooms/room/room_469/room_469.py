"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_469.room_469_partition import partition
from randomizer.entities.rooms.room.room_469.room_469_exits import exits
from randomizer.entities.rooms.room.room_469.room_469_events import events
from randomizer.entities.rooms.room.room_469.room_469_objects import objects

room = Room(
    partition=partition,
    music=M56_FACTORY,
    entrance_event=E2605_FACTORY_1ST_ROOM_BEFORE_FIGHT_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
