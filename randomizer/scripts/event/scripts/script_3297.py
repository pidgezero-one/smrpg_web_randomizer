# pylint: disable=C0301

"""E3297_SEA_SHOP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [OpenShop(SH07_SEA_AND_SHIP_SHAMAN), FadeInFromBlack(sync=False), Return()]
)
