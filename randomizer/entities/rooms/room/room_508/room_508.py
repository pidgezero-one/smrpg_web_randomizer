"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_508.room_508_partition import partition
from randomizer.entities.rooms.room.room_508.room_508_exits import exits
from randomizer.entities.rooms.room.room_508.room_508_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E3925_FACTORY_SAVE_ROOM_LOADERS,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
