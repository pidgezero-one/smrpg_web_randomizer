# E0402_SHYSTER_HARASSING_EASTERN_GUARD

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_707C_5),
        SetBit(TEMP_707C_6),
        SetBit(TEMP_707C_7),
        RunEventAsSubroutine(E1189_HENCHMAN_BATTLE_PACK_SELECTOR),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        PauseActionScript(NPC_9),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=17, y=113, z=4, direction=EAST),
                ASFaceSouthwest(),
            ],
        ),
        StartAsyncEmbeddedActionScript(
            target=NPC_9,
            prefix=0xF1,
            subscript=[
                ASTransferToXYZF(x=17, y=114, z=4, direction=EAST),
                ASFaceNortheast(),
                ASSetSolidityBits(cant_walk_through=True),
            ],
        ),
        SetBit(TEMP_7049_6),
        RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
        FadeInFromBlack(sync=False),
        Pause(30),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        SetSyncActionScript(NPC_9, A0098_WALK_RANDOM_DIRECTIONS_NO_SOLIDITY_CHANGE),
        Return(),
    ]
)
