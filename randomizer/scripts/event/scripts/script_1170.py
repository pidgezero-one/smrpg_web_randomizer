# pylint: disable=C0301

"""E1170_SEASIDE_HEALTH_FOOD_SHOP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [OpenShop(SH16_SEASIDE_HEALTH_FOOD), FadeInFromBlack(sync=False), Return()]
)
