# E3191_ACTIVATE_POST_MINES_BOSS_FIRST_MINECART_SESSION

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MINECART_CLEARED, ["EVENT_3191_ret_9"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(60),
                ASSetSpriteSequence(
                    index=8,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASFaceSoutheast(),
                ASResetProperties(),
            ],
        ),
        RunEventAsSubroutine(E1394_FOUR_DIGIT_COIN_VALUE_HANDLER),
        ActionQueueAsync(target=SCREEN_FOCUS, subscript=[ASShiftEastSteps(4)]),
        CloseDialog(),
        Jmp(["EVENT_3190_stop_all_background_events_0"]),
        Return(identifier="EVENT_3191_ret_9"),
    ]
)
