# pylint: disable=C0301

"""E0410_BED_SHYSTER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_704A_2),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
        RunEventAsSubroutine(E1010_SHYSTER_SUBROUTINE),
        SetBit(OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_1_DEFEATED),
        JmpIfObjectInCurrentLevel(NPC_2, ["EVENT_410_fade_in_from_black_async_48"]),
        SetBit(OCCUPIED_MUSHROOM_KINGDOM_HOUSE_SHYSTER_2_DEFEATED),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASTransferToXYZF(x=7, y=44, z=6, direction=EAST),
                ASFaceNorthwest(),
            ]),
        FadeInFromBlack(sync=False),
        PauseActionScript(NPC_2),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(NORMAL),
                ASWalkSoutheastSteps(2),
            ]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        Pause(10),
        Pause(10),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASWalkSouthwestSteps(2),
                ASWalkSoutheastSteps(2),
                ASFaceNortheast(),
            ]),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceSouthwest()]),
        PauseActionScript(NPC_0),
        SetVarToConst(TEMP_70A9, 20),
        RunEventAsSubroutine(E0278_UNKNOWN),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASFaceSouthwest(),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ]),
        Pause(30),
        SetSyncActionScript(NPC_0, A0023_FAST_REPEATED_JUMPING),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASWalkNorthwestSteps(5),
                ASWalkSouthwestSteps(5),
                ASDb(bytearray(b"\xfd\xf2")),
                ASVisibilityOff(),
            ]),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
        FadeInFromBlack(sync=False, identifier="EVENT_410_fade_in_from_black_async_48"),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
    ]
)
