"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_269.room_269_partition import partition
from randomizer.entities.rooms.room.room_269.room_269_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3805_ENDING_CREDITS_CORONATION_LOADER,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[])
