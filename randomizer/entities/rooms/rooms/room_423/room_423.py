from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_423.room_423_partition import partition
from randomizer.entities.rooms.rooms.room_423.room_423_exits import exits
from randomizer.entities.rooms.rooms.room_423.room_423_events import events
from randomizer.entities.rooms.rooms.room_423.room_423_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E1766_TEMPLE_ELEVATOR_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
