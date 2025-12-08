# pylint: disable=C0301

"""E2346_TOWER_THWOMP_SEESAW_CONTD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_1, subscript=[ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)]
        ),
        SetSyncActionScript(NPC_1, A0738_TOWER_CHEST_SEESAW_WHEN_ACTIVATED),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASPlaySound(sound=SO073_THWOMP_STOMP, channel=4),
                ASJumpToHeight(128),
                ASPause(32),
            ]),
        ActionQueueSync(target=NPC_0, subscript=[ASShiftZUpPixels(4)]),
        Pause(1),
        SetAsyncActionScript(NPC_1, A0739_TOWER_SEESAW_CHEST_ITEM),
        JmpIfMarioInAir(["EVENT_2346_clear_bit_9"]),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 23, ["EVENT_2346_enable_controls_11"]),
        ClearBit(TEMP_7043_0, identifier="EVENT_2346_clear_bit_9"),
        Return(),
        EnableControls([], identifier="EVENT_2346_enable_controls_11"),
        FreezeCamera(),
        ActionQueueSync(target=MARIO, subscript=[ASJumpToHeight(384)]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FASTER), ASShiftZUpSteps(16)]),
        Pause(32),
        FadeOutToBlack(sync=False, duration=16),
        SetBit(DIRECTIONAL_7045_0),
        EnterArea(
            room_id=R035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS,
            face_direction=SOUTHEAST,
            x=3,
            y=53,
            z=0,
            run_entrance_event=True),
        Return(),
    ]
)
