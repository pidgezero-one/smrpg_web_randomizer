from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_28.room_28_partition import partition
from randomizer.entities.rooms.rooms.room_28.room_28_exits import exits
from randomizer.entities.rooms.rooms.room_28.room_28_events import events
from randomizer.entities.rooms.rooms.room_28.room_28_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E3282_SHIP_BOSS_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
