from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_268.room_268_partition import partition
from randomizer.entities.rooms.rooms.room_268.room_268_exits import exits
from randomizer.entities.rooms.rooms.room_268.room_268_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E1771_TEMPLE_BOSS_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
