from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_5.room_5_partition import partition
from randomizer.entities.rooms.rooms.room_5.room_5_exits import exits
from randomizer.entities.rooms.rooms.room_5.room_5_events import events
from randomizer.entities.rooms.rooms.room_5.room_5_objects import objects

room = Room(
    partition=partition,
    music=M39_MARRYMORE,
    entrance_event=E0610_MARRYMORE_OCCUPIED_EXTERIOR_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
