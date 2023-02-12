from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_133.room_133_partition import partition
from randomizer.entities.rooms.rooms.room_133.room_133_exits import exits
from randomizer.entities.rooms.rooms.room_133.room_133_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E3285_SEA_SINGLE_CHEST_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Swim,
        ExtraSpriteActions.Whirl,
    ],
)
