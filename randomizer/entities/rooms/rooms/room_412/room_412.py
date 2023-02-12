from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_412.room_412_partition import partition
from randomizer.entities.rooms.rooms.room_412.room_412_exits import exits
from randomizer.entities.rooms.rooms.room_412.room_412_events import events
from randomizer.entities.rooms.rooms.room_412.room_412_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3725_NIMBUS_CASTLE_NOTE_HALLWAY_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
