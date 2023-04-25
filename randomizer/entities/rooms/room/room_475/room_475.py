"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_475.room_475_partition import partition
from randomizer.entities.rooms.room.room_475.room_475_exits import exits
from randomizer.entities.rooms.room.room_475.room_475_events import events
from randomizer.entities.rooms.room.room_475.room_475_objects import objects

room = Room(
    partition=partition,
    music=M67_WEAPONS_FACTORY,
    entrance_event=E1891_ABYSS_BIG_CONVEYOR_ROOM_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[],
)
