# pylint: disable=C0301

"""E1140_SEASIDE_OCCUPIED_BOMB_SHOP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [OpenShop(SH08_SEASIDE_TOWN_MINION), FadeInFromBlack(sync=False), Return()]
)
