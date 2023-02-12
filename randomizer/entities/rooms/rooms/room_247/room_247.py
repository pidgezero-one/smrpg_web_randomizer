from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_247.room_247_partition import partition

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1521_CLONE_RESERVED,
    event_tiles=[],
    exit_fields=[],
    objects=[],
    extra_sprite_actions=[],
)
