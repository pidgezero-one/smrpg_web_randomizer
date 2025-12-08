"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_400.room_400_partition import partition
from randomizer.entities.rooms.room.room_400.room_400_exits import exits
from randomizer.entities.rooms.room.room_400.room_400_events import events
from randomizer.entities.rooms.room.room_400.room_400_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E2224_KEEP_FINAL_BOSS_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.RECOIL,
        ExtraSpriteActions.WOBBLE,
    ])
