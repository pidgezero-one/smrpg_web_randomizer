# Logic module for Bowser Door randomization.

import inspect
import random
import enum

from randomizer import data
from randomizer.logic import flags
from randomizer.logic.patch import Patch
from randomizer.management.disassembler_common import use_table_name
from randomizer.helpers.eventtables import room_table



class ExitType(enum.Enum):
    Tile = enum.auto()
    Background = enum.auto()

class BowserDoorRoom:
    room = 0
    to_proceed = 0
    to_return = None
    proceed_index = 0
    return_index = None

    def __init__(self, room, to_proceed, proceed_index, exit_type=ExitType.Tile, to_return=None, return_index=None):
        self.room = room # room ID
        self.to_proceed = to_proceed # event script ID
        self.to_return = to_return # event script ID
        self.exit_type = exit_type # ExitType enum
        self.proceed_index = proceed_index # target index in room.events array
        self.return_index = return_index # target index in room.events array

    def __str__(self):
        return '<{}: room {}>'.format(self.__class__.__name__, self.room)


def randomize_all(world):
    if world.settings.is_flag_enabled(flags.BowserDoorShuffle):
        doors = [
            BowserDoorRoom(321, 1958, 0, ExitType.Tile, 1878, 1),
            BowserDoorRoom(322, 1960, 0, ExitType.Tile, 1879, 1),
            BowserDoorRoom(376, 1950, 4),
            BowserDoorRoom(377, 1944, 4),
            BowserDoorRoom(455, 1945, 0, ExitType.Tile, None, 1),
            BowserDoorRoom(456, 1947, 0, ExitType.Tile, None, 1),
            BowserDoorRoom(457, 1942, 0, ExitType.Tile, 1935, 1),
            BowserDoorRoom(458, 1943, 0, ExitType.Tile, 1946, 1),
            BowserDoorRoom(459, 1962, 4),
            BowserDoorRoom(460, 1948, 4),
            BowserDoorRoom(461, 1949, 4),
            BowserDoorRoom(462, 1964, 4),
            BowserDoorRoom(463, 1954, 1951, ExitType.Background),
            BowserDoorRoom(464, 1966, 1953, ExitType.Background),
            BowserDoorRoom(465, 1956, 0),
            BowserDoorRoom(466, 1952, 0),
            BowserDoorRoom(467, 1968, 1955, ExitType.Background),
            BowserDoorRoom(468, 3353, 0)
        ]

        # get each set of 3 rooms
        random.shuffle(doors)
        hallways = [
            doors[0:3],
            doors[3:6],
            doors[6:9],
            doors[9:12],
            doors[12:15],
            doors[15:18]
        ]
        # set the hallway entrance events for each door
        world.eventscripts[1957][0]["args"] = [hallways[0][0].to_proceed]
        world.eventscripts[1959][0]["args"] = [hallways[1][0].to_proceed]
        world.eventscripts[1961][0]["args"] = [hallways[2][0].to_proceed]
        world.eventscripts[1963][0]["args"] = [hallways[3][0].to_proceed]
        world.eventscripts[1965][0]["args"] = [hallways[4][0].to_proceed] 
        world.eventscripts[1967][0]["args"] = [hallways[5][0].to_proceed]
        # for h in hallways:
        #     print(['%s' % (use_table_name('Rooms', room_table, d.room)) for d in h])
        # for i in range(0, 6):
        #     print(hallways[i][0].to_proceed)

        for hall in hallways:
            first_room = hall[0]
            second_room = hall[1]
            third_room = hall[2]
            # first room
            # if first room in the hallway, do not allow to go backwards
            if first_room.return_index is not None:
                world.rooms[first_room.room]["event_tiles"][first_room.return_index]["event"] = 256
            # if this room has a normal exit, write the next room's loader into its designated exit event trigger
            if first_room.exit_type == ExitType.Tile:
                world.rooms[first_room.room]["event_tiles"][first_room.proceed_index]["event"] = second_room.to_proceed
            # if this room has an automatic exit (barrel counting, quiz, coins), write the next room's loader into its designated exit event
            else:
                world.eventscripts[first_room.proceed_index][0]["args"] = [second_room.to_proceed]
            # middle room
            if second_room.return_index is not None:
                world.rooms[second_room.room]["event_tiles"][second_room.return_index]["event"] = first_room.to_return if first_room.to_return is not None else 256
            if second_room.exit_type == ExitType.Tile:
                world.rooms[second_room.room]["event_tiles"][second_room.proceed_index]["event"] = third_room.to_proceed
            else:
                world.eventscripts[second_room.proceed_index][0]["args"] = [third_room.to_proceed]
            # final room
            if third_room.return_index is not None:
                world.rooms[third_room.room]["event_tiles"][third_room.return_index]["event"] = second_room.to_return if second_room.to_return is not None else 256
            # final room must always exit with 3350
            if third_room.exit_type == ExitType.Tile:
                world.rooms[third_room.room]["event_tiles"][third_room.proceed_index]["event"] = 3350
            else:
                world.eventscripts[third_room.proceed_index][0]["args"] = [3350]

        
        # Bowser's Keep threshold
        value = world.settings.get_flag(flags.BowserDoorRequirements).value
        for c, cmd in enumerate(world.eventscripts[3350]):
            if cmd["command"] == 'jmp_if_var_equals_const' and cmd["args"][0] == 0x70b6 and cmd["args"][1] == 4:
                cmd = world.eventscripts[3350][c]["args"][1] = value
