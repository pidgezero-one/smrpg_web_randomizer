# pylint: disable=C0301

"""E1674_LANDS_END_ENTER_GROTTO"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetSyncActionScript(MARIO, A0161_SEQUENCE_LOOPING_OFF),
        PlaySound(sound=SO032_UNDERGROUND_WARP, channel=6),
        StartAsyncEmbeddedActionScript(
            target=MARIO,
            prefix=0xF1,
            subscript=[
                ASFloatingOff(),
                ASSetSpriteSequence(
                    index=15, sprite_offset=1, is_sequence=True, looping=True
                ),
                ASStartLoopNTimes(7),
                ASVisibilityOn(),
                ASPause(1),
                ASVisibilityOff(),
                ASShiftZUpPixels(1),
                ASEndLoop(),
            ]),
        PixelateLayers(
            layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=8, duration=196
        ),
        EnterArea(
            room_id=R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS,
            face_direction=NORTHWEST,
            x=17,
            y=103,
            z=11),
        SetBit(DIRECTIONAL_7049_0),
        EnableControls([]),
        FadeInFromBlack(sync=True),
        ActionQueueSync(
            target=MARIO, subscript=[ASJumpToHeight(height=0, silent=True)]
        ),
        PauseScriptUntilEffectDone(),
        Jmp(["EVENT_1676_set_8"]),
    ]
)
