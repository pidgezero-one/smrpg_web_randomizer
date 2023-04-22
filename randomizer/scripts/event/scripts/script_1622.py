# pylint: disable=C0301

"""E1622_BUCKET_WARP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToTappedButton(),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_1622_ret_10"]),
        Set7000ToPressedButton(),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_1622_ret_10"]),
        PlaySound(sound=SO032_UNDERGROUND_WARP, channel=6),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetSpriteSequence(
                    index=15, sprite_offset=1, is_sequence=True, looping=True
                ),
                ASSetWalkingSpeed(SLOW),
                ASWalkToXYCoords(x=3, y=62),
                ASStartLoopNTimes(11),
                ASVisibilityOn(),
                ASPause(2),
                ASVisibilityOff(),
                ASShiftZDownPixels(1),
                ASEndLoop(),
            ],
        ),
        PixelateLayers(
            layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=8, duration=196
        ),
        JmpIfBitSet(FACTORY_BOSS_DEFEATED, ["EVENT_1622_set_bit_7"]),
        JmpIfBitSet(BUCKET_WARP_ENABLED, ["EVENT_1622_bucket_warp"]),
        SetBit(BUCKET_WARP_BIT, identifier="EVENT_1622_set_bit_7"),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        EnterArea(
            room_id=R069_MIDAS_RIVER_WATERFALL,
            face_direction=SOUTH,
            x=9,
            y=108,
            z=0,
            run_entrance_event=True,
        ),
        Return(identifier="EVENT_1622_ret_10"),
        SetBit(BUCKET_WARP_DIRECTIONAL_BIT, identifier="EVENT_1622_bucket_warp"),
        JmpToEvent(E2651_BUCKET_WARP_CHECK_GRANTER),
    ]
)
