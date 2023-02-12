from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_106.room_106_partition import partition
from randomizer.entities.rooms.rooms.room_106.room_106_exits import exits
from randomizer.entities.rooms.rooms.room_106.room_106_events import events

room = Room(
    partition=partition,
    music=M47_GRATE_GUYS_CASINO,
    entrance_event=E2648_CASINO_EXTERIOR_LOADER,
    events=events,
    exits=exits,
    objects=[],
    extra_sprite_actions=[]
)
