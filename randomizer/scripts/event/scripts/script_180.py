# pylint: disable=C0301

"""E0180_NPC_QUEST_3_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([Set7000ToCurrentLevel(), JmpToEvent(E0251_NPC_QUEST_3_GRANT)])
