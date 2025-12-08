# pylint: disable=C0301

"""E3943_SHOES_CHEST"""

from randomizer.scripts.event.script_imports import *
from randomizer.entities.items.items import Shoes

script = EventScript(
    [
        RunEventAsSubroutine(E0033_OLD_CHEST_LOADER_POSSIBLY_UNUSED),
        CreatePacketAt7010(
            packet=P099_SHOES_CHEST, destinations=["EVENT_3943_ret_259"]
        ),
        AddToInventory(Shoes),
        PlaySound(sound=SO014_FLOWER, channel=6),
        RunDialog(
            dialog_id=DI2096_GOT_SHOES,
            above_object=MARIO,
            closable=False,
            sync=True,
            multiline=False,
            use_background=False,
            bit_6=True),
        Inc(WEDDING_GEAR_COUNTER),
        Return(identifier="EVENT_3943_ret_259"),
    ]
)
