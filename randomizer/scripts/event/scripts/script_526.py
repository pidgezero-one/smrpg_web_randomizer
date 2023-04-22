# pylint: disable=C0301

"""E0526_ROSE_TOWN_EQUIP_SHOP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [OpenShop(SH02_ROSE_TOWN_ARMOR), FadeInFromBlack(sync=False), Return()]
)
