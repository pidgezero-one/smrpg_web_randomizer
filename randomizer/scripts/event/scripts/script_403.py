# pylint: disable=C0301

"""E0403_SHYSTER_HARASSING_WALLET_GUY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1190_HENCHMAN_BATTLE_PACK_SELECTOR),
        SetBit(TEMP_704A_2),
        SetVarToConst(TEMP_70A9, 26),
        RunEventAsSubroutine(E1010_SHYSTER_SUBROUTINE),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                )
            ]),
        PauseActionScript(NPC_7),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=14, y=119, z=0, direction=EAST),
                ASFaceSouthwest(),
            ]),
        StartAsyncEmbeddedActionScript(
            target=NPC_7,
            prefix=0xF1,
            subscript=[
                ASTransferToXYZF(x=14, y=120, z=0, direction=EAST),
                ASFaceNortheast(),
                ASSetSolidityBits(cant_walk_through=True),
                ASSetSolidityBits(bit_0=True),
            ]),
        RememberLastObject(),
        FadeInFromBlack(sync=False),
        Pause(30),
        RunDialog(
            dialog_id=DI0668_THAT_WAS_TOO_DARN_CLOSE,
            above_object=NPC_7,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        UnsyncDialog(),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6])
            ]),
        SetSyncActionScript(NPC_7, A0128_WALK_RANDOM_DIRECTIONS),
        Return(),
    ]
)
