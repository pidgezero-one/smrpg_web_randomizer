# pylint: disable=C0301

"""E1296_TOWER_CHECKERBOARD_ROOM_FIREBALL_LAUNCHER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            TEMP_7043_0, ["EVENT_1296_ret_11"], identifier="EVENT_1296_jmp_if_bit_set_0"
        ),
        Pause(1),
        CreatePacketAtObjectCoords(
            packet=P034_GREY_EXPLOSION_SFX,
            target_npc=MARIO,
            destinations=["EVENT_1296_jmp_if_bit_set_0"]),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASTransferToXYZF(x=20, y=23, z=0, direction=EAST),
                ASWalkSoutheastPixels(8),
                ASWalkSouthwestPixels(8),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=8, is_sequence=True, looping=True),
                ASSetPriority(3),
                ASVisibilityOn(),
                ASPause(10),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASSetSpriteSequence(index=9, is_sequence=True, looping=True),
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftNorthSteps(3),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
                ASPause(30),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[ASJumpToHeight(height=80, silent=True), ASPause(40)]),
        StartBattleAtBattlefield(143, BF12_BOOSTER_TOWER),
        JmpIfBitClear(GAME_OVER, ["EVENT_1296_set_bit_8"]),
        ResetAndChooseGame(),
        SetBit(TEMP_7043_0, identifier="EVENT_1296_set_bit_8"),
        ActionQueueSync(target=NPC_4, subscript=[ASVisibilityOff()]),
        FadeInFromBlack(sync=False),
        Return(identifier="EVENT_1296_ret_11"),
    ]
)
