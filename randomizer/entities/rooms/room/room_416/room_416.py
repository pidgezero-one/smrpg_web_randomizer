"""Room import"""
from randomizer.entities.rooms.room_imports import *
from randomizer.entities.rooms.room.room_416.room_416_partition import partition
from randomizer.entities.rooms.room.room_416.room_416_exits import exits
from randomizer.entities.rooms.room.room_416.room_416_events import events
from randomizer.entities.rooms.room.room_416.room_416_objects import objects

room = Room(
    partition=partition,
    music=M50_NIMBUS_LAND,
    entrance_event=E3642_NIMBUS_EXTERIOR_OCCUPIED_LOADER,
    events=events,
    exits=exits,
    objects=objects,
    extra_sprite_actions=[])
