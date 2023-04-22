# pylint: disable=C0301

"""E0176_CHEST_5_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([Set7000ToCurrentLevel(), JmpToEvent(E0243_CHEST_5_GRANT)])
