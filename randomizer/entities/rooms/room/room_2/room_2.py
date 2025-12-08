"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_2.room_2_partition import partition

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E2496_START_GAME,
    events=[],
    exits=[],
    objects=[],
    extra_sprite_actions=[])
