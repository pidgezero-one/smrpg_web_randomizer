"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_474.room_474_partition import partition
from randomizer.entities.rooms.room.room_474.room_474_exits import exits
from randomizer.entities.rooms.room.room_474.room_474_events import events
from randomizer.entities.rooms.room.room_474.room_474_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E1897_ABYSS_UPPER_MACHINE_YARID_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.TUMBLE_BACK,
    ],
)
