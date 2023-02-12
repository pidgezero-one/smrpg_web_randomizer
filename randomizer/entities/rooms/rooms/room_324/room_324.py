from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_324.room_324_partition import partition
from randomizer.entities.rooms.rooms.room_324.room_324_exits import exits
from randomizer.entities.rooms.rooms.room_324.room_324_events import events
from randomizer.entities.rooms.rooms.room_324.room_324_objects import objects

room = Room(
    partition=partition,
    music=M51_MONSTRO_TOWN,
    entrance_event=E2048_MONSTRO_TOWN_EXTERIOR_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
