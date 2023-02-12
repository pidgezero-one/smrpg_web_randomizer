from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_294.room_294_partition import partition

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=[],
    extra_sprite_actions=[],
)
