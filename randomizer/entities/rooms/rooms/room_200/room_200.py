from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_200.room_200_partition import partition
from randomizer.entities.rooms.rooms.room_200.room_200_exits import exits
from randomizer.entities.rooms.rooms.room_200.room_200_objects import objects

room = Room(
    partition=partition,
    music=M32_AND_MY_NAMES_BOOSTER,
    entrance_event=E1341_ELDER_KEY_PRIZE_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
