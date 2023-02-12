from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_289.room_289_partition import partition
from randomizer.entities.rooms.rooms.room_289.room_289_exits import exits
from randomizer.entities.rooms.rooms.room_289.room_289_events import events
from randomizer.entities.rooms.rooms.room_289.room_289_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E0592_MINES_BOSS_ROOM_LOADER_BEFORE_DEFEAT,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
