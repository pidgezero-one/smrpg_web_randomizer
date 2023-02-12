from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_176.room_176_partition import partition
from randomizer.entities.rooms.rooms.room_176.room_176_exits import exits
from randomizer.entities.rooms.rooms.room_176.room_176_events import events
from randomizer.entities.rooms.rooms.room_176.room_176_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E3284_SHIP_SAVE_ROOMS_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
