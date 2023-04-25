"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_433.room_433_partition import partition
from randomizer.entities.rooms.room.room_433.room_433_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E3925_FACTORY_SAVE_ROOM_LOADERS,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
