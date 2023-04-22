# pylint: disable=C0301

"""E3182_MINECART_PAID_LOBBY_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, OW24_MOLEVILLE),
        JmpIfBitSet(TEMP_7042_0, ["EVENT_3182_set_bit_3"]),
        JmpToSubroutine(["EVENT_3183_jmp_if_bit_set_4"]),
        SetBit(DIRECTIONAL_7049_0, identifier="EVENT_3182_set_bit_3"),
        ActionQueueSync(
            target=MARIO, subscript=[ASJumpToHeight(height=0, silent=True)]
        ),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER),
    ]
)
