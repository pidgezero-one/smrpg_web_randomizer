from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_427.room_427_partition import partition
from randomizer.entities.rooms.rooms.room_427.room_427_events import events
from randomizer.entities.rooms.rooms.room_427.room_427_objects import objects

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E1584_TEMPLE_FINAL_ROOM_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.DownPipe,
    ],
)
