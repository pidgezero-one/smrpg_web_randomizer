from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_43.room_43_partition import partition
from randomizer.entities.rooms.rooms.room_43.room_43_exits import exits
from randomizer.entities.rooms.rooms.room_43.room_43_events import events
from randomizer.entities.rooms.rooms.room_43.room_43_objects import objects

room = Room(
    partition=partition,
    music=M31_BOOSTERS_TOWER,
    entrance_event=E1312_TOWER_LOBBY_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
