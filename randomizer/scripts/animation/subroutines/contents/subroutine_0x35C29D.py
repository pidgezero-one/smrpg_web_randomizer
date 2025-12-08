# pylint: disable=C0301,C0103

"""referenced by ally_spells Shocker"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=64,
    script=[
        ClearAMEM16Bit(0x60, identifier="queuestart_0x35c29d"),
        ClearAMEM16Bit(0x6E),
        ObjectQueueAtOffsetAndIndex(index=2, target_address=0x35C293),
        ObjectQueueAtOffsetAndIndex(index=4, target_address=0x35C293),
        PauseScriptUntilAMEMBitsSet(0x6E, [0]),
        PauseScriptUntilAMEMBitsSet(0x6F, [0]),
        SetOMEMMainToAMEM8Bit(omem=0x6F, amem=0x6F),
        ReturnObjectQueue(),
        PlaySound(sound=S0094_SHOCKER, identifier="queuestart_0x35c2b4"),
        ScreenEffect(SEF0003_SHOCKER),
        Db(bytearray(b"\xa8\x02\x00")),
        SetAMEM8BitToConst(0x6F, 1),
        SetOMEMMainToAMEM8Bit(omem=0x6F, amem=0x6F),
        ReturnObjectQueue(),
        StartTrackingAllyButtonInputs(identifier="queuestart_0x35c2c4"),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=35),
        TimingForOneTieredButtonPress(
            end_accepting_input=30,
            start_accepting_input=0,
            partial_start=15,
            perfect_start=20,
            perfect_end=30,
            destinations=["command_0x35c2d3"]),
        PlaySound(sound=S0078_TIMED_STAT_BOOST),
        EndTrackingAllyButtonInputs(identifier="command_0x35c2d3"),
        SetAMEM8BitToConst(0x6E, 1),
        SetOMEMMainToAMEM8Bit(omem=0x6E, amem=0x6E),
        ReturnObjectQueue(),
    ])
