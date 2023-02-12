from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_177.room_177_partition import partition
from randomizer.entities.rooms.rooms.room_177.room_177_exits import exits
from randomizer.entities.rooms.rooms.room_177.room_177_events import events
from randomizer.entities.rooms.rooms.room_177.room_177_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E3224_SHIP_PASSWORD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
