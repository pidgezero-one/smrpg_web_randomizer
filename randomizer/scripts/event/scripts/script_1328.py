# pylint: disable=C0301

"""E1328_TOWER_EXTERIOR_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1605_TOWER_EXTERIOR_CANCEL_EXP_STAR),
        PlayMusicAtDefaultVolume(M13_ROAD_IS_FULL_OF_DANGERS),
        RunEventAsSubroutine(E0878_TOWER_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER),
        JmpIfBitSet(TOWER_OPENED, ["EVENT_1328_remove_from_current_level_3_"]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASWalkSoutheastPixels(2),
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetPriority(0),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ]),
        ActionQueueAsync(target=NPC_5, subscript=[ASWalkNortheastPixels(8)]),
        Jmp(["EVENT_1328_fade_in_from_black_async_4_"]),
        RemoveObjectFromCurrentLevel(
            NPC_1, identifier="EVENT_1328_remove_from_current_level_3_"
        ),
        RemoveObjectFromCurrentLevel(NPC_2),
        ApplySolidityModToLevel(
            permanent=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=0
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R202_BOOSTER_TOWER_ENTRANCE, mod_id=32
        ),
        FadeInFromBlack(
            sync=False, identifier="EVENT_1328_fade_in_from_black_async_4_"
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1328_jmp_if_bit_set_22"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1328_jmp_if_bit_set_22"]),
        RunEventAsSubroutine(E3899_BOOSTER_TOWER_STAR_PIECE_SIGNAL),
        JmpIfBitClear(
            GAMEBOY_KID_PURCHASE_COMPLETE,
            ["EVENT_1328_ret_26"],
            identifier="EVENT_1328_jmp_if_bit_set_22"),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(identifier="EVENT_1328_ret_26"),
    ]
)
