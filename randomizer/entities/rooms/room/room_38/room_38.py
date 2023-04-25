"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_38.room_38_partition import partition
from randomizer.entities.rooms.room.room_38.room_38_exits import exits

room = Room(
    partition=partition,
    music=M32_AND_MY_NAMES_BOOSTER,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=[],
    extra_sprite_actions=[],
)
