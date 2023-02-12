from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_251.room_251_partition import partition
from randomizer.entities.rooms.rooms.room_251.room_251_exits import exits
from randomizer.entities.rooms.rooms.room_251.room_251_events import events
from randomizer.entities.rooms.rooms.room_251.room_251_objects import objects

room = Room(
    partition=partition,
    music=M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
    entrance_event=E2476_BEAN_VALLEY_5_PIPE_AREA_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DownPipe,
    ]
)
