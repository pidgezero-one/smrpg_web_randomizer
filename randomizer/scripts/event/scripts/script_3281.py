# pylint: disable=C0301

"""E3281_SHIP_UPPER_HENCHMAN_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            SHIP_PRE_BOSS_BATTLE_2_CLEARED, ["EVENT_3281_run_event_as_subroutine_3"]
        ),
        ActionQueueSync(target=NPC_0, subscript=[ASShiftToXYCoords(x=13, y=114)]),
        ActionQueueSync(target=NPC_1, subscript=[ASShiftToXYCoords(x=13, y=116)]),
        RunEventAsSubroutine(
            E0804_SHIP_2ND_PREBOSS_BATTLE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        RunEventAsSubroutine(
            E0015_STANDARD_ROOM_LOADER,
            identifier="EVENT_3281_run_event_as_subroutine_3"),
        JmpIfBitSet(SHIP_PRE_BOSS_BATTLE_2_CLEARED, ["EVENT_3281_ret_31"]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASWalkToXYCoords(x=15, y=121),
                ASSequenceLoopingOn(),
                ASFaceSouthwest(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASWalkToXYCoords(x=15, y=120),
                ASSequenceLoopingOn(),
                ASFaceSouthwest(),
            ]),
        Pause(60),
        RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
        SetBit(TEMP_707C_5),
        ClearBit(TEMP_707C_6),
        ClearBit(TEMP_707C_7),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        JmpIfBitSet(RUN_AWAY, ["EVENT_3281_run_event_at_return_32"]),
        FadeInFromBlack(sync=False),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetAllSpeeds(NORMAL),
                ASFixedFCoordOn(),
                ASSequenceLoopingOff(),
                ASWalk1StepNortheast(),
                ASFixedFCoordOff(),
            ]),
        Pause(20),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetAllSpeeds(NORMAL),
                ASSequenceLoopingOff(),
                ASWalk1StepSoutheast(),
                ASFaceNorthwest(),
            ]),
        ActionQueueAsync(target=NPC_1, subscript=[ASWalkNortheastSteps(2)]),
        Pause(15),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM,
            mod_id=0),
        SetBit(TEMP_7043_0),
        SetBit(SHIP_PRE_BOSS_BATTLE_2_CLEARED),
        ActionQueueAsync(
            target=NPC_1, subscript=[ASWalk1StepNorthwest(), ASFaceSoutheast()]
        ),
        Return(identifier="EVENT_3281_ret_31"),
        RunEventAtReturn(
            E3306_SHIP_LOWER_HENCHMAN_ROOM_LOADER_CONTINUED,
            identifier="EVENT_3281_run_event_at_return_32"),
        Return(),
    ]
)
