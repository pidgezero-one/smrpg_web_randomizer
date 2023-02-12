from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_284.room_284_partition import partition
from randomizer.entities.rooms.rooms.room_284.room_284_exits import exits
from randomizer.entities.rooms.rooms.room_284.room_284_events import events
from randomizer.entities.rooms.rooms.room_284.room_284_objects import objects

room = Room(
    partition=partition,
    music=M33_MOLEVILLE,
    entrance_event=E3156_MINECART_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.PraiseFront,
        ExtraSpriteActions.Yoshi,
    ]
)
