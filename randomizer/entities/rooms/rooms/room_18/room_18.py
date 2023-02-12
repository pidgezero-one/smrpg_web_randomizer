from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_18.room_18_partition import partition
from randomizer.entities.rooms.rooms.room_18.room_18_exits import exits
from randomizer.entities.rooms.rooms.room_18.room_18_objects import objects

room = Room(
    partition=partition,
    music=M02_MUSHROOM_KINGDOM,
    entrance_event=E0322_MUSHROOM_KINGDOM_THRONE_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
