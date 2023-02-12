from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_439.room_439_partition import partition

room = Room(
    partition=partition,
    music=M11_BOWSERS_CASTLE_1ST_TIME,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=[],
    extra_sprite_actions=[],
)
