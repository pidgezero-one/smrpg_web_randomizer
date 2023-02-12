from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_98.room_98_partition import partition
from randomizer.entities.rooms.rooms.room_98.room_98_exits import exits
from randomizer.entities.rooms.rooms.room_98.room_98_events import events
from randomizer.entities.rooms.rooms.room_98.room_98_objects import objects

room = Room(
    partition=partition,
    music=M18_ROSE_TOWN,
    entrance_event=E0537_ROSE_TOWN_TREASURE_HOUSE_2F_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
