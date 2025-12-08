# pylint: disable=C0301

"""E0405_TABLE_SHYSTER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_704A_2),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        RunEventAsSubroutine(E1187_HENCHMAN_BATTLE_PACK_SELECTOR),
        RunEventAsSubroutine(E1010_SHYSTER_SUBROUTINE),
        JmpIfObjectInSpecificLevel(
            NPC_3,
            R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
            ["EVENT_405_fade_in_from_black_async_24"]),
        PauseActionScript(NPC_0, identifier="EVENT_405_pause_action_script_6"),
        PauseActionScript(NPC_1),
        PauseActionScript(NPC_2),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASFixedFCoordOff(),
                ASTransferToXYZF(x=5, y=20, z=4, direction=EAST),
                ASFaceNortheast(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASFixedFCoordOff(),
                ASTransferToXYZF(x=4, y=21, z=4, direction=EAST),
                ASFaceNortheast(),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASFixedFCoordOff(),
                ASTransferToXYZF(x=5, y=22, z=4, direction=EAST),
                ASFaceNortheast(),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=5, y=19, z=4, direction=EAST),
                ASFaceSouthwest(),
            ]),
        RememberLastObject(),
        SetBit(TEMP_7049_6),
        RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
        FadeInFromBlack(sync=False),
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
            ["EVENT_405_fade_in_from_black_async_24_"]),
        ActionQueueAsync(target=NPC_0, subscript=[ASPause(60), ASFaceSouthwest()]),
        UnsyncDialog(),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASAddZCoord1Step(),
                ASDecZCoord1Step(),
            ]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASWalk1StepNorthwest(),
                ASWalkSouthwestSteps(3),
                ASWalkNorthwestSteps(1),
                ASWalkNortheastSteps(2),
                ASVisibilityOff(),
            ]),
        SetBit(OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_1_DEFEATED),
        Return(),
        FadeInFromBlack(sync=False, identifier="EVENT_405_fade_in_from_black_async_24"),
        Return(),
        FadeInFromBlack(
            sync=False, identifier="EVENT_405_fade_in_from_black_async_24_"
        ),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        Return(),
    ]
)
