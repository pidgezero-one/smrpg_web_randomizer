from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_86.room_86_partition import partition
from randomizer.entities.rooms.rooms.room_86.room_86_exits import exits
from randomizer.entities.rooms.rooms.room_86.room_86_objects import objects

room = Room(
    partition=partition,
    music=M18_ROSE_TOWN,
    entrance_event=E0261_FADE_MUSIC_ROOM_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DownPipe,
    ],
)
