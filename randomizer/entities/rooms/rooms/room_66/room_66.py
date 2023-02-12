from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.rooms.room_66.room_66_partition import partition
from randomizer.entities.rooms.rooms.room_66.room_66_exits import exits
from randomizer.entities.rooms.rooms.room_66.room_66_events import events

room = Room(
    partition=partition,
    music=M13_ROAD_IS_FULL_OF_DANGERS,
    entrance_event=E3917_ROSE_WAY_BACK_ENTRANCE_LOADER,
    events=events,
    exits=exits,
    objects=[],
    extra_sprite_actions=[]
)
