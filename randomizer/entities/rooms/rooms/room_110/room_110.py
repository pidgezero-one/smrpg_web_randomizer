from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_110.room_110_partition import partition
from randomizer.entities.rooms.rooms.room_110.room_110_exits import exits
from randomizer.entities.rooms.rooms.room_110.room_110_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E2112_NIMBUS_CASTLE_STATUE_GAME_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Salute,
        ExtraSpriteActions.Recoil,
        ExtraSpriteActions.Dizzy,
    ],
)
