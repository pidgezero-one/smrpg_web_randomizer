from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_250.room_250_partition import partition

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E1522_CLONE_RESERVED,
    event_tiles=[],
    exit_fields=[],
    objects=[],
    extra_sprite_actions=[],
)
