# pylint: disable=C0301

"""E0600_MARRYMORE_OCCUPIED_CHAPEL_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set0158Bit7Offset(0x015E),
        Set0158Bit7Offset(0x0160),
        Set0158Bit7Offset(0x0162),
        JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_257_fade_in_from_black_async_0"]),
        JmpIfBitClear(CHAPEL_ITEM_RETRIEVAL_STARTED, ["EVENT_600_ret_12"]),
        JmpIfBitClear(CHAPEL_ITEM_RETRIEVAL_STARTED, ["EVENT_600_sequence_setter"]),
        RunEventAsSubroutine(E3930_MARRYMORE_GEAR_PRELOADER),
        RunEventAsSubroutine(
            E0790_MARRYMORE_OCCUPIED_SANCTUARY_SHUFFLED_NPC_ANIMATION_LOADER,
            identifier="EVENT_600_sequence_setter"),
        FadeInFromBlack(sync=True),
        Return(identifier="EVENT_600_ret_12"),
    ]
)
