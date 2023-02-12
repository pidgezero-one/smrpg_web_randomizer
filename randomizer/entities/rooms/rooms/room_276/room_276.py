from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_276.room_276_partition import partition
from randomizer.entities.rooms.rooms.room_276.room_276_exits import exits
from randomizer.entities.rooms.rooms.room_276.room_276_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3184_MINES_FIRST_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
