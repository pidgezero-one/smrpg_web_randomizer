from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_69.room_69_partition import partition
from randomizer.entities.rooms.rooms.room_69.room_69_objects import objects

room = Room(
    partition=partition,
    music=M22_MIDAS_RIVER,
    entrance_event=E3480_MIDAS_RIVER_WATERFALL_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
