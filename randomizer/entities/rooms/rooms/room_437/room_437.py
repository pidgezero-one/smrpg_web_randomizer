from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_437.room_437_partition import partition
from randomizer.entities.rooms.rooms.room_437.room_437_exits import exits
from randomizer.entities.rooms.rooms.room_437.room_437_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3736_NIMBUS_CASTLE_FINAL_HALLWAY_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
