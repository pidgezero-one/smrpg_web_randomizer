from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_331.room_331_partition import partition
from randomizer.entities.rooms.rooms.room_331.room_331_exits import exits
from randomizer.entities.rooms.rooms.room_331.room_331_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
