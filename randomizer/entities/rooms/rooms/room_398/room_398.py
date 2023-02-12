from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_398.room_398_partition import partition
from randomizer.entities.rooms.rooms.room_398.room_398_exits import exits
from randomizer.entities.rooms.rooms.room_398.room_398_objects import objects

room = Room(
    partition=partition,
    music=M51_MONSTRO_TOWN,
    entrance_event=E2051_MONSTRO_SHOP_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
