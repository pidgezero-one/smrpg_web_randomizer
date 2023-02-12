from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_365.room_365_partition import partition
from randomizer.entities.rooms.rooms.room_365.room_365_exits import exits

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=[],
    extra_sprite_actions=[],
)
