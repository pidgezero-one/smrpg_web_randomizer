from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_267.room_267_partition import partition
from randomizer.entities.rooms.rooms.room_267.room_267_exits import exits
from randomizer.entities.rooms.rooms.room_267.room_267_events import events
from randomizer.entities.rooms.rooms.room_267.room_267_objects import objects

room = Room(
    partition=partition,
    music=M51_MONSTRO_TOWN,
    entrance_event=E2090_MONSTRO_ENTRANCE_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[]
)
