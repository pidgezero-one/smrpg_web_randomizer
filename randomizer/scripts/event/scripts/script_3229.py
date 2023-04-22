# pylint: disable=C0301

"""E3229_SHIP_CLONE_TRANSFORM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
        StopAllBackgroundEvents(),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASPlaySound(sound=SO044_GHOST_FLOAT, channel=4),
                ASTransferToObjectXY(NPC_0),
                ASSet700CToObjectCoord(target_npc=NPC_0, coord=COORD_F, pixel=True),
                ASFaceEast7C(),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASStartLoopNTimes(3),
                ASVisibilityOff(),
                ASPause(8),
                ASVisibilityOn(),
                ASPause(8),
                ASEndLoop(),
                ASStartLoopNTimes(3),
                ASVisibilityOff(),
                ASPause(4),
                ASVisibilityOn(),
                ASPause(4),
                ASEndLoop(),
                ASStartLoopNTimes(3),
                ASVisibilityOff(),
                ASPause(2),
                ASVisibilityOn(),
                ASPause(2),
                ASEndLoop(),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASStartLoopNTimes(3),
                ASVisibilityOn(),
                ASPause(8),
                ASVisibilityOff(),
                ASPause(8),
                ASEndLoop(),
                ASStartLoopNTimes(3),
                ASVisibilityOn(),
                ASPause(4),
                ASVisibilityOff(),
                ASPause(4),
                ASEndLoop(),
                ASStartLoopNTimes(3),
                ASVisibilityOn(),
                ASPause(2),
                ASVisibilityOff(),
                ASPause(2),
                ASEndLoop(),
                ASVisibilityOn(),
                ASFaceMario(),
                ASPause(2),
            ],
        ),
        ClearBit(TEMP_707C_5),
        SetBit(TEMP_707C_6),
        SetBit(TEMP_707C_7),
        SetVarToConst(BATTLE_PACK_ID, 77),
        RunEventAsSubroutine(E0016_FIGHT_REMOVE_PERMANENTLY),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASDb(bytearray(b"\xfd\xf2")),
                ASClearSolidityBits(
                    cant_pass_walls=True,
                    bit_4=True,
                    cant_pass_npcs=True,
                    cant_walk_through=True,
                    bit_7=True,
                ),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASDb(bytearray(b"\xfd\xf2")),
                ASClearSolidityBits(
                    cant_pass_walls=True,
                    bit_4=True,
                    cant_pass_npcs=True,
                    cant_walk_through=True,
                    bit_7=True,
                ),
            ],
        ),
        Return(),
    ]
)
