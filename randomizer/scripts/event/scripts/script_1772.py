# E1772_LANDS_END_BULLET_BILL

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        ActionQueueSync(
            target=MEM_70A8, subscript=[ASSetVRAMPriority(NORMAL_PRIORITY)]
        ),
        JmpIfMarioOnAnObjectOrNot(["EVENT_1772_ret_7", "EVENT_1772_ret_7"]),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=3,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASFloatingOn(),
            ],
        ),
        RunBackgroundEvent(
            event_id=E1773_LANDS_END_BULLET_BILL_BACKGROUND,
            return_on_level_exit=True,
            bit_6=True,
        ),
        Return(identifier="EVENT_1772_ret_7"),
    ]
)
