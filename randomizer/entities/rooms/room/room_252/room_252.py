"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_252.room_252_partition import partition
from randomizer.entities.rooms.room.room_252.room_252_exits import exits
from randomizer.entities.rooms.room.room_252.room_252_events import events
from randomizer.entities.rooms.room.room_252.room_252_objects import objects

room = Room(
    partition=partition,
    music=M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
    entrance_event=E2466_BEAN_VALLEY_1ST_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
