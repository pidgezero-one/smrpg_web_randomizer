from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_482.room_482_partition import partition
from randomizer.entities.rooms.rooms.room_482.room_482_exits import exits
from randomizer.entities.rooms.rooms.room_482.room_482_events import events
from randomizer.entities.rooms.rooms.room_482.room_482_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0339_MUSHROOM_KINGDOM_OCCUPIED_RAZ_RAINI_HOUSE_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
