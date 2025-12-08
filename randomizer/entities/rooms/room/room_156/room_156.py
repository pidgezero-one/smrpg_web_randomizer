"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_156.room_156_partition import partition
from randomizer.entities.rooms.room.room_156.room_156_exits import exits
from randomizer.entities.rooms.room.room_156.room_156_events import events

room = Room(
    partition=partition,
    music=M39_MARRYMORE,
    entrance_event=E0261_FADE_MUSIC_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=[],
    extra_sprite_actions=[])
