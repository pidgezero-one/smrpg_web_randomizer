# pylint: disable=C0301

"""E1275_MUSHROOM_KINGDOM_OCCUPIED_EXTERIOR_HENCHMAN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_707C_6),
        ClearBit(TEMP_707C_7),
        SetBit(TEMP_707C_5),
        RunEventAsSubroutine(E1188_HENCHMAN_BATTLE_PACK_SELECTOR),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        PauseActionScript(MEM_70A8),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASBPL262728(),
                ASVisibilityOff(),
                ASTransferToXYZF(x=11, y=18, z=4, direction=EAST),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
