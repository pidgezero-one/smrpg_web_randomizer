from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_424.room_424_partition import partition
from randomizer.entities.rooms.rooms.room_424.room_424_exits import exits
from randomizer.entities.rooms.rooms.room_424.room_424_events import events

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E1778_TEMPLE_GENERIC_PIPE_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=[],
    extra_sprite_actions=[
        ExtraSpriteActions.DownPipe,
    ]
)
