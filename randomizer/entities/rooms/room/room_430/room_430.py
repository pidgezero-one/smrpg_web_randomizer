"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_430.room_430_partition import partition
from randomizer.entities.rooms.room.room_430.room_430_objects import objects

room = Room(
    partition=partition,
    music=M50_NIMBUS_LAND,
    entrance_event=E0738_NIMBUS_LAND_FINAL_BOSS_FIGHT_TOWN_SQUARE_LOADER,
    events=[],
    exits=[],
    objects=objects,
    extra_sprite_actions=[
        ExtraSpriteActions.CHALLENGE_NIMBUS,
    ])
