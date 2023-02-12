from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_259.room_259_partition import partition
from randomizer.entities.rooms.rooms.room_259.room_259_exits import exits
from randomizer.entities.rooms.rooms.room_259.room_259_objects import objects

room = Room(
    partition=partition,
    music=M32_AND_MY_NAMES_BOOSTER,
    entrance_event=E2338_TOWER_BUTTON_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
