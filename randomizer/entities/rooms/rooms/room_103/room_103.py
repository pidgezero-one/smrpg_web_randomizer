from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_103.room_103_partition import partition
from randomizer.entities.rooms.rooms.room_103.room_103_events import events
from randomizer.entities.rooms.rooms.room_103.room_103_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E1893_ABYSS_BOSS_2_ROOM_LOADER,
    events=events,
    exit_fields=[],
    objects=objects,
    extra_sprite_actions=[],
)
