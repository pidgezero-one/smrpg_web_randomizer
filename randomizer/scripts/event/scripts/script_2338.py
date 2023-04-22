# pylint: disable=C0301

"""E2338_TOWER_BUTTON_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(
            BOOSTER_PASS_SECRET_OPEN, ["EVENT_2338_fade_in_from_black_async_3"]
        ),
        DisableObjectTrigger(NPC_0),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_mold=True, is_sequence=True, looping=True
                ),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASOverwriteSolidity(),
            ],
        ),
        FadeInFromBlack(sync=False, identifier="EVENT_2338_fade_in_from_black_async_3"),
        Return(),
    ]
)
