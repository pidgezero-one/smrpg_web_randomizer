from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_42.room_42_partition import partition
from randomizer.entities.rooms.rooms.room_42.room_42_exits import exits
from randomizer.entities.rooms.rooms.room_42.room_42_events import events
from randomizer.entities.rooms.rooms.room_42.room_42_objects import objects

room = Room(
    partition=partition,
    music=M32_AND_MY_NAMES_BOOSTER,
    entrance_event=E2576_TOWER_8BIT_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
