# pylint: disable=C0301

"""E1181_JUICE_BAR_TENOR_CARD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [OpenShop(SH11_JUICE_BAR_TENOR), FadeInFromBlack(sync=False), Return()]
)
