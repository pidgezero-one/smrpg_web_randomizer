"""A0047_SKY_BRIDGE_BULLET_BILL"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(3),
        Db(bytearray(b"\xc8#")),
        AddConstToVar(X_COORD_2, 224),
        AddConstToVar(Y_COORD_2, 112),
        AddConstToVar(Z_COORD_2, 384),
        TransferTo70167018701A(),
        PlaySound(sound=SO113_OPEN_CHAMBER_DOOR, channel=4),
        VisibilityOn(),
        SetVarToConst(TEMP_7034, 65535),
        CreatePacketAtObjectCoords(
            packet=P032_BLUE_CLOUD,
            target_npc=DUMMY_0X07,
            destinations=["ACTION_47_set_animation_speed_10"]),
        SetAllSpeeds(FAST, identifier="ACTION_47_set_animation_speed_10"),
        SetBit(TEMP_7044_5),
        WalkSoutheastSteps(2),
        SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
        WalkSoutheastSteps(15),
        SetVRAMPriority(NORMAL_PRIORITY),
        WalkSoutheastSteps(12),
        VisibilityOff(),
        Return(),
    ]
)
