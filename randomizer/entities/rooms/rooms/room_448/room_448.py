from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_448.room_448_partition import partition
from randomizer.entities.rooms.rooms.room_448.room_448_exits import exits
from randomizer.entities.rooms.rooms.room_448.room_448_objects import objects

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E3924_KEEP_1ST_SAVE_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DispleasedFront,
        ExtraSpriteActions.SurpriseFrame,
        ExtraSpriteActions.Wobble,
    ],
)
