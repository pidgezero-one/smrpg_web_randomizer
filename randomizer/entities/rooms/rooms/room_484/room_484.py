from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_484.room_484_partition import partition

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=[],
    extra_sprite_actions=[],
)
