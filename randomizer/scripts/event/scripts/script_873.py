# pylint: disable=C0301

"""E0873_TEST_SCRIPT_7"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [StartBattleAtBattlefield(176, BF35_MARRYMORE_CHAPEL_SANCTUARY), Return()]
)
