# pylint: disable=C0301

"""E3773_HOT_SPRINGS_EJECT_FROM_WATER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FreezeCamera(),
        EnableControlsUntilReturn([]),
        ActionQueueAsync(
            target=MARIO, subscript=[ASWalkToXYCoords(x=17, y=114), ASFaceSouth()]
        ),
        PaletteSetMorphs(palette_type=FADE_TO, palette_set=10, duration=142, row=8),
        Pause(60),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(height=80, silent=True),
                ASWalkSouthwestPixels(8),
                ASSetSpriteSequence(
                    index=0, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASWalkSouthwestSteps(2),
                ASSetWalkingSpeed(NORMAL),
                ASPause(
                    1, identifier="EVENT_3773_action_queue_async_5_SUBSCRIPT_pause_6"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3773_action_queue_async_5_SUBSCRIPT_pause_6"]
                ),
                ASPause(30),
                ASResetProperties(),
                ASStartLoopNTimes(19),
                ASTurnClockwise45DegreesNTimes(1),
                ASPause(2),
                ASEndLoop(),
                ASSetSpriteSequence(
                    index=15, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(4),
                ASSetSpriteSequence(
                    index=12, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(50),
                ASResetProperties(),
            ]),
        PaletteSet(palette_set=84, row=1),
        UnfreezeCamera(),
        Return(),
    ]
)
