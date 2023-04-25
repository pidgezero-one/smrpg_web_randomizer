"""Event script exports"""

from randomizer.types.overworld_scripts.event_scripts.classes import (
    EventScriptController,
)
from .bank_1e import bank as event_script_bank_1
from .bank_1f import bank as event_script_bank_2
from .bank_20 import bank as event_script_bank_3

event_controller = EventScriptController(
    [event_script_bank_1, event_script_bank_2, event_script_bank_3]
)
