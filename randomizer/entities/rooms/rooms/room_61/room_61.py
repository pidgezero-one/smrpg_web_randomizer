from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_61.room_61_partition import partition

room = Room(
    partition=partition,
    music=M50_NIMBUS_LAND,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=[],
    extra_sprite_actions=[],
)
