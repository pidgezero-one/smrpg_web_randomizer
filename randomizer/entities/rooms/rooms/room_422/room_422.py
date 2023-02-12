from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_422.room_422_partition import partition
from randomizer.entities.rooms.rooms.room_422.room_422_exits import exits
from randomizer.entities.rooms.rooms.room_422.room_422_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E1810_TEMPLE_VAULT_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
