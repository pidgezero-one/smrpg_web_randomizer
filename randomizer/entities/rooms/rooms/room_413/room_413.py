from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_413.room_413_partition import partition
from randomizer.entities.rooms.rooms.room_413.room_413_exits import exits
from randomizer.entities.rooms.rooms.room_413.room_413_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3811_NIMBUS_INNER_CELLAR_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
