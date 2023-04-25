"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_112.room_112_partition import partition
from randomizer.entities.rooms.room.room_112.room_112_exits import exits
from randomizer.entities.rooms.room.room_112.room_112_events import events
from randomizer.entities.rooms.room.room_112.room_112_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E2108_NIMBUS_CASTLE_STATUE_POLISHER_BOSS_FIGHT_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
