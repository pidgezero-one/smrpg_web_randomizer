"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_476.room_476_partition import partition
from randomizer.entities.rooms.room.room_476.room_476_exits import exits
from randomizer.entities.rooms.room.room_476.room_476_events import events

room = Room(
    partition=partition,
    music=M66_BOWSERS_CASTLE_2ND_TIME,
    entrance_event=E2233_KEEP_1ST_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=[],
    extra_sprite_actions=[])
