"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_155.room_155_partition import partition
from randomizer.entities.rooms.room.room_155.room_155_exits import exits
from randomizer.entities.rooms.room.room_155.room_155_objects import objects

room = Room(
    partition=partition,
    music=M39_MARRYMORE,
    entrance_event=E0628_MARRYMORE_KITCHEN_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
