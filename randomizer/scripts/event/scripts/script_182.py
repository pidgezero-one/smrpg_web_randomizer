# pylint: disable=C0301

"""E0182_NPC_QUEST_5_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([Set7000ToCurrentLevel(), JmpToEvent(E0249_NPC_QUEST_5_GRANT)])
