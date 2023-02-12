from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_394.room_394_partition import partition
from randomizer.entities.rooms.rooms.room_394.room_394_exits import exits
from randomizer.entities.rooms.rooms.room_394.room_394_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3342_VOLCANO_5TH_BOSS_PATH_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
