# E3081_YOU_MISSED

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
        DisableTriggerOfObjectAt70A8InCurrentLevel(),
        SetSyncActionScript(MEM_70A8, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
        Set70107015ToObjectXYZ(MEM_70A8),
        CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 608),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
        JmpIfBitSet(UNKNOWN_704A_3, ["EVENT_3081_clear_bit_251"]),
        PlaySound(sound=SO014_FLOWER, channel=6),
        ClearBit(UNKNOWN_704A_3, identifier="EVENT_3081_clear_bit_251"),
        Inc(HIDDEN_CHEST_COUNTER),
        RunDialog(
            dialog_id=DI3321_YOU_MISSED,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        SetSyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceSouthwest(),
                ASSetSpriteSequence(
                    index=1, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=4),
            ],
        ),
        Pause(40),
        SetAsyncActionScript(MARIO, A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
    ]
)
