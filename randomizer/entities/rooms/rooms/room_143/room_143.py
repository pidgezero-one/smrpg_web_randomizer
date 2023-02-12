from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_143.room_143_partition import partition
from randomizer.entities.rooms.rooms.room_143.room_143_objects import objects

room = Room(
    partition=partition,
    music=M07_PIPE_VAULT,
    entrance_event=E0454_GOOMBA_THUMPIN_ROOM_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
