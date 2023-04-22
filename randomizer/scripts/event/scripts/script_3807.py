# pylint: disable=C0301

"""E3807_ENDING_CREDITS_RACE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R505_ENDING_CREDITS_YOSTER_ISLE_CROCO_RACING_YOSHI,
            face_direction=SOUTH,
            x=4,
            y=16,
            z=0,
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASVisibilityOff(),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
        ),
        SetTempSyncActionScript(NPC_3, A0803_INC_PALETTE_ROW),
        SetTempAsyncActionScript(NPC_2, A0803_INC_PALETTE_ROW),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASSetPriority(3),
                ASSetSpriteSequence(
                    index=1, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(1),
                ASSetSpriteSequence(
                    index=15, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASSetPaletteRow(12),
            ],
        ),
        ActionQueueSync(target=NPC_0, subscript=[ASSetPriority(3)]),
        ActionQueueSync(
            target=NPC_10,
            subscript=[ASTransferXYZFPixels(x=248, y=4, z=0, direction=EAST)],
        ),
        RememberLastObject(),
        JmpToEvent(E3806_ENDING_CREDITS_RACE_NPCS),
    ]
)
