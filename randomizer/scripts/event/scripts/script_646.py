# pylint: disable=C0301

"""E0646_MARRYMORE_SHOP_EVENT_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([OpenShop(SH05_MARRYMORE), FadeInFromBlack(sync=False), Return()])
