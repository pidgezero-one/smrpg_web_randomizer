from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_508.room_508_partition import partition
from randomizer.entities.rooms.rooms.room_508.room_508_exits import exits
from randomizer.entities.rooms.rooms.room_508.room_508_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E3925_FACTORY_SAVE_ROOM_LOADERS,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
