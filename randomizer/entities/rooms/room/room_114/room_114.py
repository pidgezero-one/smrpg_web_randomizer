"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_114.room_114_partition import partition
from randomizer.entities.rooms.room.room_114.room_114_exits import exits
from randomizer.entities.rooms.room.room_114.room_114_events import events
from randomizer.entities.rooms.room.room_114.room_114_objects import objects

room = Room(
    partition=partition,
    music=M61_VALENTINA,
    entrance_event=E3703_NIMBUS_CASTLE_TWO_LEVEL_CHEST_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.LEAN_BACK,
        ExtraSpriteActions.LEAN_BACK_2,
        ExtraSpriteActions.LEAN_FORWARD,
        ExtraSpriteActions.SURPRISE_FRAME_BACK,
        ExtraSpriteActions.FLOP,
    ])
