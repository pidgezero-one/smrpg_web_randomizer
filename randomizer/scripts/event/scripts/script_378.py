# pylint: disable=C0301

"""E0378_MUSHROOM_KINGDOM_OCCUPIED_MAIN_HALL_SHYSTER_CHASING_TOAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_707C_5),
        SetBit(TEMP_707C_7),
        SetBit(TEMP_707C_6),
        RunEventAsSubroutine(E1189_HENCHMAN_BATTLE_PACK_SELECTOR),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        StopAllBackgroundEvents(),
        PauseActionScript(NPC_5),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASTransferToXYZF(x=4, y=25, z=4, direction=EAST),
                ASVisibilityOn(),
                ASFaceNortheast(),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=5, y=24, z=4, direction=EAST),
                ASFaceSouthwest(),
            ]),
        SetBit(TEMP_7049_6),
        RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASWalkNorthwestSteps(2),
                ASVisibilityOff(),
            ]),
        RemoveObjectFromSpecificLevel(
            NPC_5, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL
        ),
        RemoveObjectFromSpecificLevel(
            NPC_4, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL
        ),
        Return(),
    ]
)
