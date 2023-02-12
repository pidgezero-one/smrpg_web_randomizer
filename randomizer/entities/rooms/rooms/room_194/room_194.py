from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_194.room_194_partition import partition
from randomizer.entities.rooms.rooms.room_194.room_194_exits import exits
from randomizer.entities.rooms.rooms.room_194.room_194_events import events
from randomizer.entities.rooms.rooms.room_194.room_194_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1344_TOWER_HENCHMAN_2_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
