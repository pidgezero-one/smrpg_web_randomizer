from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_258.room_258_partition import partition
from randomizer.entities.rooms.rooms.room_258.room_258_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1926_TOWER_BALCONY_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
