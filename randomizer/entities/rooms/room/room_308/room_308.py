"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_308.room_308_partition import partition
from randomizer.entities.rooms.room.room_308.room_308_exits import exits
from randomizer.entities.rooms.room.room_308.room_308_events import events
from randomizer.entities.rooms.room.room_308.room_308_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1124_FROG_SHOP_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
