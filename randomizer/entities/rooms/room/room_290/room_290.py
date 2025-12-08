"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_290.room_290_partition import partition
from randomizer.entities.rooms.room.room_290.room_290_exits import exits
from randomizer.entities.rooms.room.room_290.room_290_events import events
from randomizer.entities.rooms.room.room_290.room_290_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3182_MINECART_PAID_LOBBY_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
