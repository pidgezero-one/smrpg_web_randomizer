"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_406.room_406_partition import partition
from randomizer.entities.rooms.room.room_406.room_406_exits import exits
from randomizer.entities.rooms.room.room_406.room_406_events import events
from randomizer.entities.rooms.room.room_406.room_406_objects import objects

room = Room(
    partition=partition,
    music=M56_FACTORY,
    entrance_event=E2641_FACTORY_1ST_ROOM_LOADER_AFTER_FIGHT,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
