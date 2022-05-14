from ..variables import variables
from classes import EventScriptCommand, EventScriptCommandNoArgs
from constants import command_names as cmdnm
from constants.classes import EventScriptCommandName
from constants.misc import TOTAL_SCRIPTS
from ..numbers.classes import UInt16, UInt8
from ..variables.classes import Flag


# script operations


class StartLoopNFrames(EventScriptCommand):
    _command_name: EventScriptCommandName = cmdnm.START_LOOP_N_FRAMES
    length: int

    def __init__(self, length: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.length = UInt16(length)


class StartLoopNTimes(EventScriptCommand):
    _command_name: EventScriptCommandName = cmdnm.START_LOOP_N_TIMES
    count: int

    def __init__(self, count: int, identifier: str = None) -> None:
        super().__init__(identifier)
        self.count = UInt16(count)
