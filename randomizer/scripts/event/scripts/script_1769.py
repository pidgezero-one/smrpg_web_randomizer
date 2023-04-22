# pylint: disable=C0301

"""E1769_TEMPLE_SUMMON_GREEN_BUTTON"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMPLE_BOSS_BUTTON_PRESSED, ["EVENT_1769_ret_6"]),
        SetBit(TEMPLE_BOSS_BUTTON_PRESSED),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM, mod_id=0
        ),
        PlaySound(sound=SO017_OPEN_FRONT_GATE, channel=6),
        ActionQueueAsync(
            target=LAYER_1,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASShiftSouthSteps(3),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        Return(identifier="EVENT_1769_ret_6"),
    ]
)
