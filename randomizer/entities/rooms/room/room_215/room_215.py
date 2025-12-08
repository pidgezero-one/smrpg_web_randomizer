"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_215.room_215_partition import partition
from randomizer.entities.rooms.room.room_215.room_215_exits import exits
from randomizer.entities.rooms.room.room_215.room_215_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E1127_SEASIDE_OCCUPIED_HEALTH_STORE_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
