from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_136.room_136_partition import partition
from randomizer.entities.rooms.rooms.room_136.room_136_exits import exits
from randomizer.entities.rooms.rooms.room_136.room_136_events import events
from randomizer.entities.rooms.rooms.room_136.room_136_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E0015_STANDARD_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Whirl,
    ]
)
