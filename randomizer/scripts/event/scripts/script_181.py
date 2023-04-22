# pylint: disable=C0301

"""E0181_NPC_QUEST_4_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([Set7000ToCurrentLevel(), JmpToEvent(E0250_NPC_QUEST_4_GRANT)])
