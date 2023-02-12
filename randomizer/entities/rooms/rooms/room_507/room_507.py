from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_507.room_507_partition import partition
from randomizer.entities.rooms.rooms.room_507.room_507_exits import exits
from randomizer.entities.rooms.rooms.room_507.room_507_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E1892_ABYSS_BOSS_1_DEFEATED_TEMP_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
