from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_172.room_172_partition import partition
from randomizer.entities.rooms.rooms.room_172.room_172_exits import exits
from randomizer.entities.rooms.rooms.room_172.room_172_objects import objects

room = Room(
    partition=partition,
    music=M41_SUNKEN_SHIP,
    entrance_event=E3226_SHIP_GENERIC_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
