from randomizer.types.overworld_scripts.event_scripts.classes import (
    EventScriptController,
)
from .bank_1e import bank as bank_1e
from .bank_1f import bank as bank_1f
from .bank_20 import bank as bank_20

events = EventScriptController(banks=[bank_1e, bank_1f, bank_20])
