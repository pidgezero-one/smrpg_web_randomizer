"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_471.room_471_partition import partition
from randomizer.entities.rooms.room.room_471.room_471_exits import exits
from randomizer.entities.rooms.room.room_471.room_471_events import events
from randomizer.entities.rooms.room.room_471.room_471_objects import objects

room = Room(
    partition=partition,
    music=M56_FACTORY,
    entrance_event=E2617_FACTORY_2ND_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
