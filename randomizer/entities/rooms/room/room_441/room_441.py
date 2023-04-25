"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_441.room_441_partition import partition
from randomizer.entities.rooms.room.room_441.room_441_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E2292_ENDING_CREDITS_TOADOFSKY,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[],
)
