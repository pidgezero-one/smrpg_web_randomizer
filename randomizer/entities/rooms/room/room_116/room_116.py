"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_116.room_116_partition import partition
from randomizer.entities.rooms.room.room_116.room_116_exits import exits
from randomizer.entities.rooms.room.room_116.room_116_events import events
from randomizer.entities.rooms.room.room_116.room_116_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3696_NIMBUS_CASTLE_WEST_LOWER_HALL_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
