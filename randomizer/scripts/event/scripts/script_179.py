# pylint: disable=C0301

"""E0179_NPC_QUEST_2_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([Set7000ToCurrentLevel(), JmpToEvent(E0252_NPC_QUEST_2_GRANT)])
