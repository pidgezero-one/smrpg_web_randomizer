# pylint: disable=C0301

"""E1112_FROG_COIN_EMPORIUM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [OpenShop(SH06_FROG_COIN_EMPORIUM), FadeInFromBlack(sync=False), Return()]
)
