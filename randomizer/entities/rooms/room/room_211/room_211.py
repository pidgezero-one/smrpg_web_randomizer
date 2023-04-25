"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_211.room_211_partition import partition
from randomizer.entities.rooms.room.room_211.room_211_exits import exits
from randomizer.entities.rooms.room.room_211.room_211_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E1123_SEASIDE_OCCUPIED_ELDERS_HOUSE_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
