"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_397.room_397_partition import partition
from randomizer.entities.rooms.room.room_397.room_397_exits import exits
from randomizer.entities.rooms.room.room_397.room_397_events import events
from randomizer.entities.rooms.room.room_397.room_397_objects import objects

room = Room(
    partition=partition,
    music=M51_MONSTRO_TOWN,
    entrance_event=E2049_MONSTRO_SUPER_JUMP_HOUSE_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
