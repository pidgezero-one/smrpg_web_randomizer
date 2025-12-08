"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_352.room_352_partition import partition
from randomizer.entities.rooms.room.room_352.room_352_exits import exits
from randomizer.entities.rooms.room.room_352.room_352_objects import objects

room = Room(
    partition=partition,
    music=M62_BARREL_VOLCANO,
    entrance_event=E3330_VOLCANO_1ST_BOSS_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SURPRISE_FRAME,
    ])
