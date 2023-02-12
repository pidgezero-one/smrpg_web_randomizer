from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_232.room_232_partition import partition
from randomizer.entities.rooms.rooms.room_232.room_232_exits import exits
from randomizer.entities.rooms.rooms.room_232.room_232_events import events
from randomizer.entities.rooms.rooms.room_232.room_232_objects import objects

room = Room(
    partition=partition,
    music=M26_FOREST_MAZE,
    entrance_event=E0774_FOREST_MAZE_BOSS_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Recoil,
    ]
)
