"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_207.room_207_partition import partition
from randomizer.entities.rooms.room.room_207.room_207_exits import exits
from randomizer.entities.rooms.room.room_207.room_207_events import events
from randomizer.entities.rooms.room.room_207.room_207_objects import objects

room = Room(
    partition=partition,
    music=M42_STILL_THE_ROAD_IS_FULL_OF_MONSTERS,
    entrance_event=E1702_BANDITS_WAY_2_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
