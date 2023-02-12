from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_221.room_221_partition import partition
from randomizer.entities.rooms.rooms.room_221.room_221_exits import exits
from randomizer.entities.rooms.rooms.room_221.room_221_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E2361_ABYSS_AMEBOID_BUTTON_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
