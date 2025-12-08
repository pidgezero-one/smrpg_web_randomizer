"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_265.room_265_partition import partition
from randomizer.entities.rooms.room.room_265.room_265_exits import exits
from randomizer.entities.rooms.room.room_265.room_265_events import events
from randomizer.entities.rooms.room.room_265.room_265_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E1792_LANDS_END_UNDERGROUND_UPPER_PIT_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
