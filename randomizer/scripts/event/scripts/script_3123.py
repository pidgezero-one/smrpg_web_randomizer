# E3123_SEWER_DRAIN_WATER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        SetBit(SEWER_WATER_LEVEL),
        SetSyncActionScript(MEM_70A8, A0056_SEWER_WATER_DRAIN),
        PlaySound(sound=SO009_GREEN_SWITCH, channel=6),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(height=0, silent=True),
                ASClearSolidityBits(cant_pass_npcs=True),
                ASShiftZDownPixels(2),
                ASResetProperties(),
                ASSetSolidityBits(cant_pass_npcs=True),
            ],
        ),
        PlaySound(sound=SO008_WATERFALL, channel=4),
        RunDialog(
            dialog_id=DI1585_WATER_DRAINED,
            above_object=MARIO,
            closable=False,
            sync=True,
            multiline=False,
            use_background=False,
            bit_6=True,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES,
            mod_id=0,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES,
            mod_id=1,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER,
            mod_id=0,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER,
            mod_id=1,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE,
            mod_id=0,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE,
            mod_id=1,
        ),
        Return(),
    ]
)
