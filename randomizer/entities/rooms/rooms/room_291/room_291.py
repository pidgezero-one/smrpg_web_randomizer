from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_291.room_291_partition import partition

room = Room(
    partition=partition,
    music=M54_HAPPY_ADVENTURE_DELIGHFUL_ADVENTURE,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=[],
    extra_sprite_actions=[],
)
