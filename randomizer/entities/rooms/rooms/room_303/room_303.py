from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_303.room_303_partition import partition

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=[],
    extra_sprite_actions=[],
)
