from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_67.room_67_partition import partition
from randomizer.entities.rooms.rooms.room_67.room_67_exits import exits
from randomizer.entities.rooms.rooms.room_67.room_67_events import events
from randomizer.entities.rooms.rooms.room_67.room_67_objects import objects

room = Room(
    partition=partition,
    music=M22_MIDAS_RIVER,
    entrance_event=E3486_MIDAS_RIVER_BASE_AREA_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
