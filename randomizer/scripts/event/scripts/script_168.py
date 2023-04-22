# pylint: disable=C0301

"""E0168_BOSS_GRANT_STAR_PIECE_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([Set7000ToCurrentLevel(), JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE)])
