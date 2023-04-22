# pylint: disable=C0301

"""E0874_TEST_SCRIPT_8"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [StartBattleAtBattlefield(184, BF40_SMITHY_FACTORY_DOMINO__CLOAKERS_PAD), Return()]
)
