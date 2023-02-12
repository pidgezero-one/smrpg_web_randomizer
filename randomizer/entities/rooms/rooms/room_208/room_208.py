from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_208.room_208_partition import partition
from randomizer.entities.rooms.rooms.room_208.room_208_exits import exits
from randomizer.entities.rooms.rooms.room_208.room_208_events import events
from randomizer.entities.rooms.rooms.room_208.room_208_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1119_SEASIDE_OCCUPIED_EXTERIOR_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
