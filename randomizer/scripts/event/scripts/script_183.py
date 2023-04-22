# pylint: disable=C0301

"""E0183_NPC_QUEST_6_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([Set7000ToCurrentLevel(), JmpToEvent(E0248_NPC_QUEST_6_GRANT)])
