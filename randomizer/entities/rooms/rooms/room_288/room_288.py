from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_288.room_288_partition import partition
from randomizer.entities.rooms.rooms.room_288.room_288_exits import exits
from randomizer.entities.rooms.rooms.room_288.room_288_events import events
from randomizer.entities.rooms.rooms.room_288.room_288_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E3167_MINES_FINAL_SAVE_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
