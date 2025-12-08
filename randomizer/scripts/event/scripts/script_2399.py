# pylint: disable=C0301

"""E2399_ABYSS_ROOM_1_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, OW05_GATE),
        SetVarToConst(FACTORY_FALL_1, 219),
        ActionQueueAsync(target=NPC_0, subscript=[ASWalkNorthwestPixels(12)]),
        JmpIfBitClear(ABYSS_ENTRANCE_DIRECTIONAL_BIT, ["EVENT_2399_fade_in_music_10"]),
        FadeInFromBlack(sync=False),
        Return(),
        FadeInMusic(M67_WEAPONS_FACTORY, identifier="EVENT_2399_fade_in_music_10"),
        FreezeCamera(),
        PlaySound(sound=SO019_LONG_FALL, channel=6),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FASTEST), ASWalkToXYCoords(x=2, y=10)]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASTransferToXYZF(x=4, y=25, z=21, direction=EAST),
                ASWalkSouthPixels(8),
            ]),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOn(),
                ASJumpToHeight(height=0, silent=True),
                ASSetSpriteSequence(
                    index=0, sprite_offset=1, is_sequence=True, looping=True
                ),
                ASPause(
                    1, identifier="EVENT_2399_action_queue_async_16_SUBSCRIPT_pause_3"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2399_action_queue_async_16_SUBSCRIPT_pause_3"]
                ),
                ASPlaySound(sound=SO058_INSERT, channel=4),
            ]),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_2399_ret_4"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2399_ret_4"]),
        RunEventAsSubroutine(E3915_FACTORY_STAR_PIECE_SIGNAL),
        SetBit(ABYSS_ENTRANCE_DIRECTIONAL_BIT),
        Return(identifier="EVENT_2399_ret_4"),
    ]
)
