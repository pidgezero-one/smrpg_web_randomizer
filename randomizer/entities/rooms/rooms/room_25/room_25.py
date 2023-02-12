from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_25.room_25_partition import partition
from randomizer.entities.rooms.rooms.room_25.room_25_exits import exits
from randomizer.entities.rooms.rooms.room_25.room_25_events import events
from randomizer.entities.rooms.rooms.room_25.room_25_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E3281_SHIP_UPPER_HENCHMAN_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
