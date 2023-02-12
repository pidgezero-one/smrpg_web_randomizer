from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_271.room_271_partition import partition
from randomizer.entities.rooms.rooms.room_271.room_271_events import events

room = Room(
    partition=partition,
    music=M27_DUNGEON_IS_FULL_OF_MONSTERS,
    entrance_event=E0593_MINES_BOSS_ROOM_LOADER_AFTER_DEFEAT,
    events=events,
    exit_fields=[],
    objects=[],
    extra_sprite_actions=[],
)
