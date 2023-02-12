# E3199_SHYGUY_CART_PRIZE_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(RUNAWAY_MINECART_ITEM_OBTAINED, ["EVENT_3199_ret_5"]),
        JmpToEvent(E0241_FREESTANDING_1_GRANT),
        SetBit(RUNAWAY_MINECART_ITEM_OBTAINED),
        Return(identifier="EVENT_3199_ret_5"),
    ]
)
