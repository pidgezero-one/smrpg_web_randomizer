from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_192.room_192_partition import partition
from randomizer.entities.rooms.rooms.room_192.room_192_exits import exits
from randomizer.entities.rooms.rooms.room_192.room_192_events import events
from randomizer.entities.rooms.rooms.room_192.room_192_objects import objects

room = Room(
    partition=partition,
    music=M32_AND_MY_NAMES_BOOSTER,
    entrance_event=E1359_CURTAIN_GAME_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.SurpriseFrame,
    ]
)
