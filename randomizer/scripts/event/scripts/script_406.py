# pylint: disable=C0301

"""E0406_YOUNGER_BROTHER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
            ["EVENT_406_pause_action_script_9"]),
        PauseActionScript(NPC_0),
        StartAsyncEmbeddedActionScript(
            target=NPC_0,
            prefix=0xF1,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetSolidityBits(cant_pass_walls=True),
                ASJumpToHeight(height=0, silent=True),
            ]),
        Pause(1, identifier="EVENT_406_pause_3"),
        JmpIfObjectInAir(NPC_0, ["EVENT_406_pause_3"]),
        RunDialog(
            dialog_id=DI0693_JUMPING_KID_DURING_OCCUPATION,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        ActionQueueAsync(
            target=NPC_0, subscript=[ASSetSolidityBits(cant_walk_through=True)]
        ),
        SetSyncActionScript(NPC_0, A0022_SLOW_REPEATED_JUMPING),
        Return(),
        PauseActionScript(NPC_0, identifier="EVENT_406_pause_action_script_9"),
        StartAsyncEmbeddedActionScript(
            target=NPC_0,
            prefix=0xF1,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetSolidityBits(cant_pass_walls=True),
                ASJumpToHeight(height=0, silent=True),
            ]),
        Pause(1, identifier="EVENT_406_pause_11"),
        JmpIfObjectInAir(NPC_0, ["EVENT_406_pause_11"]),
        RunDialog(
            dialog_id=DI0694_JUMPING_KID_DURING_OCCUPATION_2,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        ActionQueueAsync(
            target=NPC_0, subscript=[ASSetSolidityBits(cant_walk_through=True)]
        ),
        SetSyncActionScript(NPC_0, A0023_FAST_REPEATED_JUMPING),
        Return(),
    ]
)
