from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_193.room_193_partition import partition
from randomizer.entities.rooms.rooms.room_193.room_193_exits import exits
from randomizer.entities.rooms.rooms.room_193.room_193_events import events
from randomizer.entities.rooms.rooms.room_193.room_193_objects import objects

room = Room(
    partition=partition,
    music=M32_AND_MY_NAMES_BOOSTER,
    entrance_event=E0793_TOWER_FIRST_BOBOMB_STAIRCASE_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
