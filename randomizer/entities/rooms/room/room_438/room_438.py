"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_438.room_438_partition import partition
from randomizer.entities.rooms.room.room_438.room_438_exits import exits
from randomizer.entities.rooms.room.room_438.room_438_events import events
from randomizer.entities.rooms.room.room_438.room_438_objects import objects

room = Room(
    partition=partition,
    music=M50_NIMBUS_LAND,
    entrance_event=E3673_NIMBUS_LIBERATED_TOWN_SQUARE_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
