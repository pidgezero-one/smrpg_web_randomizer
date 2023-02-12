from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_41.room_41_partition import partition
from randomizer.entities.rooms.rooms.room_41.room_41_exits import exits
from randomizer.entities.rooms.rooms.room_41.room_41_events import events
from randomizer.entities.rooms.rooms.room_41.room_41_objects import objects

room = Room(
    partition=partition,
    music=M32_AND_MY_NAMES_BOOSTER,
    entrance_event=E1295_TOWER_CHECKERBOARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
