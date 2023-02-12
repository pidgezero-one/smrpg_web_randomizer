from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_414.room_414_partition import partition
from randomizer.entities.rooms.rooms.room_414.room_414_exits import exits
from randomizer.entities.rooms.rooms.room_414.room_414_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3724_NIMBUS_CASTLE_OUTER_CELLAR_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
