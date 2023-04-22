# pylint: disable=C0301

"""E1863_CROCO_SHOP_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript([OpenShop(SH23_KEEP_2), FadeInFromBlack(sync=False), Return()])
