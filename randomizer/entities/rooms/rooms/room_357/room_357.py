from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_357.room_357_partition import partition
from randomizer.entities.rooms.rooms.room_357.room_357_exits import exits

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3332_VOLCANO_1ST_BOSS_PATH_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=[],
    extra_sprite_actions=[],
)
