# pylint: disable=C0301

"""E3185_PA_MOLE_IN_DEEP_MINES"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(ITEM_ID, BambinoBomb),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3185_set_399"]),
        RunDialog(
            dialog_id=DI1632_PA_MOLE_NEEDS_BOMB,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
        SetVarToConst(TEMP_70AE, 20, identifier="EVENT_3185_set_399"),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        Pause(1),
        Store02To0248(),
        SetBit(BAMBINO_BOMB_UNKNOWN),
        Pause(2),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES,
            mod_id=32),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R272_MOLEVILLE_MINES_AREA_11_BOMBED_ROOM_WSINGING_MOLES,
            mod_id=0),
        Pause(2),
        ClearBit(BAMBINO_BOMB_UNKNOWN),
        Store00To0248(),
        Pause(1),
        JmpIfBitClear(TEMP_7043_5, ["EVENT_3185_action_queue_sync_414"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASWalk1StepSoutheast(),
                ASWalkNortheastSteps(2),
                ASWalk1StepNorthwest(),
                ASFaceSouthwest(),
                ASSetAllSpeeds(NORMAL),
            ],
            identifier="EVENT_3185_action_queue_sync_414"),
        SetVarToConst(TEMP_70AE, 20),
        SetSyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        SetSyncActionScript(MARIO, A0670_NOD_YES),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASPause(16),
                ASFaceSouthwest(),
                ASSetAllSpeeds(VERY_FAST),
                ASSequenceLoopingOn(),
                ASJumpToHeight(72),
                ASPause(20),
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASWalkToXYCoords(x=6, y=24),
                ASWalkToXYCoords(x=4, y=20),
                ASWalkSouthwestSteps(2),
                ASDb(bytearray(b"\xfd\xf2")),
                ASVisibilityOff(),
            ]),
        SetBit(MINES_BACK_OPENED),
        RemoveOneOfItemFromInventory(BambinoBomb),
        Return(),
    ]
)
