from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_393.room_393_partition import partition
from randomizer.entities.rooms.rooms.room_393.room_393_exits import exits
from randomizer.entities.rooms.rooms.room_393.room_393_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E3344_VOLCANO_FINAL_TRAMPOLINE_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
