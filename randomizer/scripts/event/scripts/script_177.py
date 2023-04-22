# pylint: disable=C0301

"""E0177_CHEST_6_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([Set7000ToCurrentLevel(), JmpToEvent(E0242_CHEST_6_GRANT)])
