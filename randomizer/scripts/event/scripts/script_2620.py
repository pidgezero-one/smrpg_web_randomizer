# pylint: disable=C0301

"""E2620_FACTORY_3RD_ROOM_BACKGROUND_NPCS_BONK_CONVEYOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_2620_pause_0"),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_2620_clear_bit_5"]),
        JmpIfBitSet(TEMP_7043_4, ["EVENT_2620_clear_bit_12"]),
        JmpIfBitSet(TEMP_7043_5, ["EVENT_2620_clear_bit_19"]),
        Jmp(["EVENT_2620_pause_0"], identifier="EVENT_2620_jmp_4"),
        ClearBit(TEMP_7043_3, identifier="EVENT_2620_clear_bit_5"),
        SetVarToConst(X_COORD_1, 8),
        SetVarToConst(Y_COORD_1, 96),
        SetVarToConst(Z_COORD_1, 12),
        Db(bytearray(b"\xfd\xc4")),
        CreatePacketAt7010(
            packet=P049_HAMMER_SPARKS_SFX, destinations=["EVENT_2620_jmp_4"]
        ),
        Jmp(["EVENT_2620_pause_0"]),
        ClearBit(TEMP_7043_4, identifier="EVENT_2620_clear_bit_12"),
        SetVarToConst(X_COORD_1, 10),
        SetVarToConst(Y_COORD_1, 101),
        SetVarToConst(Z_COORD_1, 12),
        Db(bytearray(b"\xfd\xc4")),
        CreatePacketAt7010(
            packet=P049_HAMMER_SPARKS_SFX, destinations=["EVENT_2620_jmp_4"]
        ),
        Jmp(["EVENT_2620_pause_0"]),
        ClearBit(TEMP_7043_5, identifier="EVENT_2620_clear_bit_19"),
        SetVarToConst(X_COORD_1, 13),
        SetVarToConst(Y_COORD_1, 107),
        SetVarToConst(Z_COORD_1, 12),
        Db(bytearray(b"\xfd\xc4")),
        CreatePacketAt7010(
            packet=P049_HAMMER_SPARKS_SFX, destinations=["EVENT_2620_jmp_4"]
        ),
        Jmp(["EVENT_2620_pause_0"]),
    ]
)
