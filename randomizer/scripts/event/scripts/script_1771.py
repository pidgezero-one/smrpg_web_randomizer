# pylint: disable=C0301

"""E1771_TEMPLE_BOSS_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_4,
            R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM,
            ["EVENT_1771_jmp_if_bit_clear_10"],
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASVisibilityOn(),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ],
        ),
        JmpIfBitClear(
            TEMPLE_BOSS_BUTTON_PRESSED,
            ["EVENT_1771_fade_in_from_black_async_7"],
            identifier="EVENT_1771_jmp_if_bit_clear_10",
        ),
        Jmp(["EVENT_1771_apply_solidity_mod_3"]),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM,
            mod_id=0,
            identifier="EVENT_1771_apply_solidity_mod_3",
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASVisibilityOn(),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        ActionQueueAsync(
            target=LAYER_1,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftSouthSteps(3),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        RunEventAsSubroutine(E0814_TEMPLE_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False, identifier="EVENT_1771_fade_in_from_black_async_7"),
        Return(),
    ]
)
