# pylint: disable=C0301

"""E1182_JUICE_BAR_SOPRANO_CARD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [OpenShop(SH12_JUICE_BAR_SOPRANO), FadeInFromBlack(sync=False), Return()]
)
