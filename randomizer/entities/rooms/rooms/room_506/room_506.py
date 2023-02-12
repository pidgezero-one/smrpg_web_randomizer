from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_506.room_506_partition import partition
from randomizer.entities.rooms.rooms.room_506.room_506_objects import objects

room = Room(
    partition=partition,
    music=M00_CURRENT,
    entrance_event=E2294_ENDING_CREDITS_WEDDING_LOADER,
    event_tiles=[],
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
