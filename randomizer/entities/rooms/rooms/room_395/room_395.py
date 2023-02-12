from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_395.room_395_partition import partition
from randomizer.entities.rooms.rooms.room_395.room_395_exits import exits
from randomizer.entities.rooms.rooms.room_395.room_395_events import events
from randomizer.entities.rooms.rooms.room_395.room_395_objects import objects

room = Room(
    partition=partition,
    music=M51_MONSTRO_TOWN,
    entrance_event=E2057_MONSTROMAMA_HOUSE_1F_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
