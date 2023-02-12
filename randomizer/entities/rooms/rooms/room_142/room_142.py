from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_142.room_142_partition import partition
from randomizer.entities.rooms.rooms.room_142.room_142_exits import exits
from randomizer.entities.rooms.rooms.room_142.room_142_events import events
from randomizer.entities.rooms.rooms.room_142.room_142_objects import objects

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E1722_SKY_BRIDGE_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Whirl,
        ExtraSpriteActions.Recoil,
    ]
)
