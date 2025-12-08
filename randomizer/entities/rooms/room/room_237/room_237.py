"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_237.room_237_partition import partition
from randomizer.entities.rooms.room.room_237.room_237_exits import exits
from randomizer.entities.rooms.room.room_237.room_237_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E2595_ABYSS_SAVE_ROOM_WITH_CHEST_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
