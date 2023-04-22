# pylint: disable=C0301

"""E1124_FROG_SHOP_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASWalkNorthwestPixels(3),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
