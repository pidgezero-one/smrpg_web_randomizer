from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_62.room_62_partition import partition
from randomizer.entities.rooms.rooms.room_62.room_62_events import events
from randomizer.entities.rooms.rooms.room_62.room_62_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E3135_SEWERS_GENERIC_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DownPipe,
        ExtraSpriteActions.Swim,
    ],
)
