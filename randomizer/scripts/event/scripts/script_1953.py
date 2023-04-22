# pylint: disable=C0301

"""E1953_KEEP_QUIZ_ROOM_EXIT_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([JmpToEvent(E1954_KEEP_ENTER_BARREL_COUNT_ROOM)])
