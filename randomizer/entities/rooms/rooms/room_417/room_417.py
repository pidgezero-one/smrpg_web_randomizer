from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_417.room_417_partition import partition
from randomizer.entities.rooms.rooms.room_417.room_417_exits import exits
from randomizer.entities.rooms.rooms.room_417.room_417_objects import objects

room = Room(
    partition=partition,
    music=M18_ROSE_TOWN,
    entrance_event=E2316_GARDENER_EXTERIOR_LOADER,
    event_tiles=[],
    exits=exits,
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.Climb,
    ],
)
