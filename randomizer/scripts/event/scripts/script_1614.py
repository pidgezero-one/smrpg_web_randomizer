# pylint: disable=C0301

"""E1614_MOLEVILLE_SWAP_SHOP_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutMusicToVolume(duration=1, volume=96),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_sequence=True, looping=True, mirror_sprite=True
                )
            ],
        ),
        JmpIfBitSet(MINECART_CLEARED, ["EVENT_1614_fade_in_from_black_async_5"]),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromCurrentLevel(NPC_2),
        FadeInFromBlack(sync=False, identifier="EVENT_1614_fade_in_from_black_async_5"),
        Return(),
    ]
)
