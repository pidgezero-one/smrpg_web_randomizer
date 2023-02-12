from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_161.room_161_partition import partition
from randomizer.entities.rooms.rooms.room_161.room_161_exits import exits
from randomizer.entities.rooms.rooms.room_161.room_161_events import events
from randomizer.entities.rooms.rooms.room_161.room_161_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
