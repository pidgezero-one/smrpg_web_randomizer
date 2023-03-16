# referenced by ally_spells Snowy

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=92,
    script=[
        Db(bytearray(b" \x80\x10\x00"), identifier="queuestart_0x35c307"),
        JmpIfAMEM8BitGreaterOrEqualThanConst(0x60, 31, ["command_0x35c315"]),
        DisplayMessage(BATTLE_MESSAGE, 12),
        PauseScriptUntilDialogClosed(),
        ClearAMEM16Bit(0x60, identifier="command_0x35c315"),
        ClearAMEM8Bit(0x6D),
        ClearAMEM8Bit(0x6E),
        ClearAMEM8Bit(0x6F),
        ObjectQueueAtOffsetAndIndex(index=2, target_address=0x35C2FD),
        ObjectQueueAtOffsetAndIndex(index=4, target_address=0x35C2FD),
        ObjectQueueAtOffsetAndIndex(index=6, target_address=0x35C2FD),
        PauseScriptUntilAMEMBitsSet(0x6D, [0]),
        PauseScriptUntilAMEMBitsSet(0x6E, [0]),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        SetOMEMMainToAMEM8Bit(omem=0x6F, amem=0x6F),
        ReturnObjectQueue(),
        ScreenEffect(SEF0001_SNOWY, identifier="queuestart_0x35c337"),
        Db(bytearray(b"\xa8\x02\x00")),
        SetAMEM8BitToConst(0x6E, 1),
        SetOMEMMainToAMEM8Bit(omem=0x6E, amem=0x6E),
        ReturnObjectQueue(),
        StartTrackingAllyButtonInputs(identifier="queuestart_0x35c345"),
        TimingForRotationCount(
            end_accepting_input=35, start_accepting_input=0, max_presses=8
        ),
        EndTrackingAllyButtonInputs(),
        SetAMEM8BitToConst(0x6F, 1),
        SetOMEMMainToAMEM8Bit(omem=0x6F, amem=0x6F),
        ReturnObjectQueue(),
        PauseScriptUntil(
            condition=FRAMES_ELAPSED, frames=40, identifier="queuestart_0x35c354"
        ),
        PlaySound(sound=S0119_METEOR_SWARM),
        SetAMEM8BitToConst(0x6D, 1),
        SetOMEMMainToAMEM8Bit(omem=0x6D, amem=0x6D),
        ReturnObjectQueue(),
    ],
)
