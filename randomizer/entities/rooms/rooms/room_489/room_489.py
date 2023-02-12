from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_489.room_489_partition import partition
from randomizer.entities.rooms.rooms.room_489.room_489_exits import exits
from randomizer.entities.rooms.rooms.room_489.room_489_objects import objects

room = Room(
    partition=partition,
    music=M02_MUSHROOM_KINGDOM,
    entrance_event=E0261_FADE_MUSIC_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
