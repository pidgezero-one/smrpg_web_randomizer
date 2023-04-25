"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_97.room_97_partition import partition
from randomizer.entities.rooms.room.room_97.room_97_exits import exits
from randomizer.entities.rooms.room.room_97.room_97_events import events
from randomizer.entities.rooms.room.room_97.room_97_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0537_ROSE_TOWN_TREASURE_HOUSE_2F_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
