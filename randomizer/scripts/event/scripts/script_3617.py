# pylint: disable=C0301

"""E3617_NIMBUS_INN_BEDROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(VOLCANO_LIBERATED, ["EVENT_3617_summon_to_current_level_3"]),
        FadeInFromBlack(sync=False),
        Return(),
        SummonObjectToCurrentLevel(
            NPC_1, identifier="EVENT_3617_summon_to_current_level_3"
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetSpriteSequence(index=5, is_sequence=True, looping=True),
                ASTransferXYZFPixels(x=250, y=250, z=0, direction=EAST),
            ]),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R346_NIMBUS_LAND_INN_BEDROOM, mod_id=1
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
