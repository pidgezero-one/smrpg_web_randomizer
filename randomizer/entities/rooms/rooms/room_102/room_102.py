from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_102.room_102_partition import partition
from randomizer.entities.rooms.rooms.room_102.room_102_exits import exits
from randomizer.entities.rooms.rooms.room_102.room_102_objects import objects

room = Room(
    partition=partition,
    music=M33_MOLEVILLE,
    entrance_event=E1644_MOLEVILLE_OCCUPIED_EXTERIOR_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
