from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_212.room_212_partition import partition
from randomizer.entities.rooms.rooms.room_212.room_212_exits import exits
from randomizer.entities.rooms.rooms.room_212.room_212_events import events
from randomizer.entities.rooms.rooms.room_212.room_212_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E1124_FROG_SHOP_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
