"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_261.room_261_partition import partition

room = Room(
    partition=partition,
    music=M11_BOWSERS_CASTLE_1ST_TIME,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=[],
    exits=[],
    objects=[],
    extra_sprite_actions=[])
