"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_37.room_37_partition import partition
from randomizer.entities.rooms.room.room_37.room_37_exits import exits
from randomizer.entities.rooms.room.room_37.room_37_events import events
from randomizer.entities.rooms.room.room_37.room_37_objects import objects

room = Room(
    partition=partition,
    music=M32_AND_MY_NAMES_BOOSTER,
    entrance_event=E2348_TOWER_BULLET_BILL_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
