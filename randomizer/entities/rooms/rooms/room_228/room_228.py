from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_228.room_228_partition import partition
from randomizer.entities.rooms.rooms.room_228.room_228_exits import exits
from randomizer.entities.rooms.rooms.room_228.room_228_events import events
from randomizer.entities.rooms.rooms.room_228.room_228_objects import objects

room = Room(
    partition=partition,
    music=M26_FOREST_MAZE,
    entrance_event=E2806_FOREST_MAZE_ROOM_BEFORE_TRUNK_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DownPipe,
    ]
)
