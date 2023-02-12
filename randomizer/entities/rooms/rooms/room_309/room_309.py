from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_309.room_309_partition import partition

room = Room(
    partition=partition,
    music=M05_SEASIDE_TOWN,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=[],
    extra_sprite_actions=[],
)
