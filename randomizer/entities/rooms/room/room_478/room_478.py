"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_478.room_478_partition import partition
from randomizer.entities.rooms.room.room_478.room_478_exits import exits
from randomizer.entities.rooms.room.room_478.room_478_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E2145_KEEP_DONUT_BRIDGE_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SURPRISE_FRAME,
    ])
