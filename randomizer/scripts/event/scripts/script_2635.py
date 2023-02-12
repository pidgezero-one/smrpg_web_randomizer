# E2635_CASINO_DOORWAY_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
                ASVisibilityOn(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
                ASVisibilityOn(),
            ],
        ),
        JmpIfBitClear(DIRECTIONAL_7046_1, ["EVENT_2635_fade_in_from_black_async_7"]),
        ApplySolidityModToLevel(
            permanent=True, room_id=R104_GRATE_GUYS_CASINO_FRONT_DOOR, mod_id=0
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASSetWalkingSpeed(FASTEST), ASShiftNorthwestPixels(8)],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASSetWalkingSpeed(FASTEST), ASShiftSoutheastPixels(8)],
        ),
        ActionQueueAsync(
            target=MARIO, subscript=[ASShiftSouthPixels(8), ASFaceSouthwest()]
        ),
        FadeInFromBlack(sync=False, identifier="EVENT_2635_fade_in_from_black_async_7"),
        Return(),
    ]
)
