# pylint: disable=C0301

"""E3184_MINES_FIRST_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, OW54_COAL_MINES_BOWSERS_KEEP),
        JmpIfBitSet(TEMP_7042_0, ["EVENT_3184_set_bit_3"]),
        JmpToSubroutine(["EVENT_3183_jmp_if_bit_set_4"]),
        SetBit(TEMP_7042_0, identifier="EVENT_3184_set_bit_3"),
        JmpIfBitSet(MINES_BOSS_2_DEFEATED, ["EVENT_3184_remove_from_current_level_62"]),
        PlayMusicAtDefaultVolume(M27_DUNGEON_IS_FULL_OF_MONSTERS),
        JmpIfBitClear(
            MOLEVILLE_MINES_ENTRANCE_GATING, ["EVENT_3184_remove_from_current_level_62"]
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetObjectMemoryBits(arg_1=0x0B, bits=[1]),
                ASWalkToXYCoords(x=19, y=27),
                ASFaceNortheast(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetObjectMemoryBits(arg_1=0x0B, bits=[1]),
                ASWalkToXYCoords(x=19, y=26),
                ASFaceNortheast(),
            ]),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER),
        RemoveObjectFromCurrentLevel(
            NPC_0, identifier="EVENT_3184_remove_from_current_level_62"
        ),
        RemoveObjectFromCurrentLevel(NPC_1),
        DisableObjectTrigger(NPC_0),
        DisableObjectTrigger(NPC_1),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER),
    ]
)
