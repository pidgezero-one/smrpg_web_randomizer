from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_195.room_195_partition import partition
from randomizer.entities.rooms.rooms.room_195.room_195_exits import exits
from randomizer.entities.rooms.rooms.room_195.room_195_objects import objects

room = Room(
    partition=partition,
    music=M31_BOOSTERS_TOWER,
    entrance_event=E1339_PORTRAIT_GAME_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
