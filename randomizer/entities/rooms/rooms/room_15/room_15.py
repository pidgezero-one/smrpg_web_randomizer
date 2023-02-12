from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_15.room_15_partition import partition

room = Room(
    partition=partition,
    music=M11_BOWSERS_CASTLE_1ST_TIME,
    entrance_event=E1385_VISTA_HILL_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=[],
    extra_sprite_actions=[],
)
