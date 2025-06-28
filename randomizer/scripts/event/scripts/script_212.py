# pylint: disable=C0301

"""E0212_NPC_QUEST_7_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([Set7000ToCurrentLevel(), JmpToEvent(E0226_NPC_QUEST_7_GRANT)])
