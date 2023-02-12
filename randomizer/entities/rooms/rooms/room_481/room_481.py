from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_481.room_481_partition import partition
from randomizer.entities.rooms.rooms.room_481.room_481_exits import exits
from randomizer.entities.rooms.rooms.room_481.room_481_objects import objects

room = Room(
    partition=partition,
    music=M15_HERES_SOME_WEAPONS,
    entrance_event=E0409_MUSHROOM_KINGDOM_OCCUPIED_JUMPING_KIDS_HOUSE_2F_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
