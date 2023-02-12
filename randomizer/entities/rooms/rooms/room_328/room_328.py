from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_328.room_328_partition import partition
from randomizer.entities.rooms.rooms.room_328.room_328_exits import exits
from randomizer.entities.rooms.rooms.room_328.room_328_events import events
from randomizer.entities.rooms.rooms.room_328.room_328_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0382_MUSHROOM_KINGDOM_OCCUPIED_TOADSTOOLS_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
