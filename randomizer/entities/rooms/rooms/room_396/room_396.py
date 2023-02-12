from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_396.room_396_partition import partition
from randomizer.entities.rooms.rooms.room_396.room_396_exits import exits
from randomizer.entities.rooms.rooms.room_396.room_396_events import events
from randomizer.entities.rooms.rooms.room_396.room_396_objects import objects

room = Room(
    partition=partition,
    music=M51_MONSTRO_TOWN,
    entrance_event=E2060_MONSTROMAMA_HOUSE_2F_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
