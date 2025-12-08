"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_69.room_69_partition import partition
from randomizer.entities.rooms.room.room_69.room_69_objects import objects

room = Room(
    partition=partition,
    music=M22_MIDAS_RIVER,
    entrance_event=E3480_MIDAS_RIVER_WATERFALL_LOADER,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[])
