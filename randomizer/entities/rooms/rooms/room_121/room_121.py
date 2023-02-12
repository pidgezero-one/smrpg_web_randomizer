from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_121.room_121_partition import partition
from randomizer.entities.rooms.rooms.room_121.room_121_exits import exits
from randomizer.entities.rooms.rooms.room_121.room_121_events import events
from randomizer.entities.rooms.rooms.room_121.room_121_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3732_NIMBUS_CASTLE_FINAL_CHEST_HALLWAY_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
