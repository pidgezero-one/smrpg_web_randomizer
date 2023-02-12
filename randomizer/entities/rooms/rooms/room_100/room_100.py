from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_100.room_100_partition import partition
from randomizer.entities.rooms.rooms.room_100.room_100_exits import exits
from randomizer.entities.rooms.rooms.room_100.room_100_events import events
from randomizer.entities.rooms.rooms.room_100.room_100_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E2308_BOOSTER_PASS_1ST_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.TumbleFront,
    ]
)
