# pylint: disable=C0301

"""E3345_VOLCANO_CHASE_SEQEUNCE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromSpecificLevel(NPC_0, R394_VOLCANO_POSTCD_AREA_05),
        RemoveObjectFromSpecificLevel(NPC_0, R394_VOLCANO_POSTCD_AREA_05),
        RemoveObjectFromSpecificLevel(NPC_1, R394_VOLCANO_POSTCD_AREA_05),
        RemoveObjectFromSpecificLevel(NPC_2, R394_VOLCANO_POSTCD_AREA_05),
        SetBit(VOLCANO_STAIRCASE_ANIMATION_COMPLETED),
        Pause(1, identifier="EVENT_3345_pause_5"),
        JmpIfObjectsAreLessThanXYStepsApart(
            MARIO, NPC_0, 0, 4, ["EVENT_3345_remove_from_current_level_8"]
        ),
        Jmp(["EVENT_3345_pause_5"]),
        RemoveObjectFromCurrentLevel(
            NPC_0, identifier="EVENT_3345_remove_from_current_level_8"
        ),
        RemoveObjectFromSpecificLevel(NPC_0, R394_VOLCANO_POSTCD_AREA_05),
        CreatePacketAtObjectCoords(
            packet=P045_TELEPORTATION_SHINE,
            target_npc=NPC_0,
            destinations=["EVENT_3345_pause_12"],
        ),
        Pause(1, identifier="EVENT_3345_pause_12"),
        JmpIfObjectsAreLessThanXYStepsApart(
            MARIO, NPC_0, 0, 2, ["EVENT_3345_pause_18"]
        ),
        Jmp(["EVENT_3345_pause_12"]),
        Pause(1, identifier="EVENT_3345_pause_18"),
        JmpIfObjectsAreLessThanXYStepsApart(
            MARIO, NPC_1, 0, 4, ["EVENT_3345_remove_from_current_level_21"]
        ),
        Jmp(["EVENT_3345_pause_18"]),
        RemoveObjectFromCurrentLevel(
            NPC_1, identifier="EVENT_3345_remove_from_current_level_21"
        ),
        RemoveObjectFromSpecificLevel(NPC_1, R394_VOLCANO_POSTCD_AREA_05),
        CreatePacketAtObjectCoords(
            packet=P045_TELEPORTATION_SHINE,
            target_npc=NPC_1,
            destinations=["EVENT_3345_pause_25"],
        ),
        Pause(1, identifier="EVENT_3345_pause_25"),
        JmpIfObjectsAreLessThanXYStepsApart(
            MARIO, NPC_2, 0, 4, ["EVENT_3345_remove_from_current_level_28"]
        ),
        Jmp(["EVENT_3345_pause_25"]),
        RemoveObjectFromCurrentLevel(
            NPC_2, identifier="EVENT_3345_remove_from_current_level_28"
        ),
        RemoveObjectFromSpecificLevel(NPC_2, R394_VOLCANO_POSTCD_AREA_05),
        CreatePacketAtObjectCoords(
            packet=P045_TELEPORTATION_SHINE,
            target_npc=NPC_2,
            destinations=["EVENT_3345_create_packet_at_npc_coords_32"],
        ),
        CreatePacketAtObjectCoords(
            packet=P045_TELEPORTATION_SHINE,
            target_npc=NPC_0,
            destinations=["EVENT_3345_ret_33"],
            identifier="EVENT_3345_create_packet_at_npc_coords_32",
        ),
        Return(identifier="EVENT_3345_ret_33"),
    ]
)
