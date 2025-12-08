"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_248.room_248_partition import partition

room = Room(
    partition=partition,
    music=M54_HAPPY_ADVENTURE_DELIGHFUL_ADVENTURE,
    entrance_event=E2304_BANK_1F_RETURN_EVENT_2,
    events=[],
    exits=[],
    objects=[],
    extra_sprite_actions=[])
