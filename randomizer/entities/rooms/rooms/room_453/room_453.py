from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_453.room_453_partition import partition
from randomizer.entities.rooms.rooms.room_453.room_453_exits import exits
from randomizer.entities.rooms.rooms.room_453.room_453_events import events
from randomizer.entities.rooms.rooms.room_453.room_453_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E2228_KEEP_DARK_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
