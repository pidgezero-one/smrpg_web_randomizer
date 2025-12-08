"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_202.room_202_partition import partition
from randomizer.entities.rooms.room.room_202.room_202_exits import exits
from randomizer.entities.rooms.room.room_202.room_202_events import events
from randomizer.entities.rooms.room.room_202.room_202_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1328_TOWER_EXTERIOR_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
