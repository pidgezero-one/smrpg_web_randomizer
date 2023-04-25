"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_266.room_266_partition import partition
from randomizer.entities.rooms.room.room_266.room_266_exits import exits
from randomizer.entities.rooms.room.room_266.room_266_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E2208_KEEP_1ST_BOSS_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
