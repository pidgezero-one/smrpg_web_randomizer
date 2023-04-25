"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_419.room_419_partition import partition
from randomizer.entities.rooms.room.room_419.room_419_exits import exits
from randomizer.entities.rooms.room.room_419.room_419_objects import objects

room = Room(
    partition=partition,
    music=M18_ROSE_TOWN,
    entrance_event=E2317_GARDENER_CLOUD_LOADER,
    events=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.CLIMB,
    ],
)
