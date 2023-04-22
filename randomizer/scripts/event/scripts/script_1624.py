# pylint: disable=C0301

"""E1624_MOLEVILLE_SHOP"""

from randomizer.scripts.event.script_imports import *

script = EventScript([OpenShop(SH04_MOLEVILLE), FadeInFromBlack(sync=False), Return()])
