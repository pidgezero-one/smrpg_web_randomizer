from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_229.room_229_partition import partition
from randomizer.entities.rooms.rooms.room_229.room_229_exits import exits
from randomizer.entities.rooms.rooms.room_229.room_229_events import events
from randomizer.entities.rooms.rooms.room_229.room_229_objects import objects

room = Room(
    partition=partition,
    music=M26_FOREST_MAZE,
    entrance_event=E1557_FOREST_MAZE_PAST_TRUNK_AREA_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DownPipe,
    ]
)
