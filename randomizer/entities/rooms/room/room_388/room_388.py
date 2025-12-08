"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_388.room_388_partition import partition
from randomizer.entities.rooms.room.room_388.room_388_exits import exits

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3339_VOLCANO_2ND_BOSS_PATH_ROOM_LOADER,
    events=[],
    exits=exits,
    objects=[],
    extra_sprite_actions=[])
