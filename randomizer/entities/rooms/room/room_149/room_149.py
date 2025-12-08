"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_149.room_149_partition import partition

room = Room(
    partition=partition,
    music=M30_LONG_LONG_AGO,
    entrance_event=E1551_BANK_1F_RETURN_EVENT,
    events=[],
    exits=[],
    objects=[],
    extra_sprite_actions=[])
