from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_378.room_378_partition import partition
from randomizer.entities.rooms.rooms.room_378.room_378_exits import exits
from randomizer.entities.rooms.rooms.room_378.room_378_events import events
from randomizer.entities.rooms.rooms.room_378.room_378_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3770_BEAN_VALLEY_1ST_VINE_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Climb,
    ]
)
