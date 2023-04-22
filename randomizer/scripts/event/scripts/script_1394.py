# pylint: disable=C0301

"""E1394_FOUR_DIGIT_COIN_VALUE_HANDLER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfVarEqualsConst(
            MINECART_COINS, 200, ["EVENT_1394_set_7000_to_7000_short_mem_6"]
        ),
        StoreCoinCountTo7000(),
        Dec7000FromCoins(),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=OLD_STAR_PIECE_ID),
        SetVarToConst(MINECART_COINS, 200),
        Return(),
        CopyVarToVar(
            from_var=OLD_STAR_PIECE_ID,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_1394_set_7000_to_7000_short_mem_6",
        ),
        AddCoins(PRIMARY_TEMP_7000),
        Return(),
    ]
)
