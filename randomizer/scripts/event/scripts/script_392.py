# pylint: disable=C0301

"""E0392_MUSHROOM_KINGDOM_OCCUPIED_EXTERIOR_REPEATING_SHYSTERS_POSITION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO053_BOUNCE, channel=6),
        SetSyncActionScript(NPC_2, A0136_MK_OCCUPIED_EXTERIOR_REPEATING_HENCHMEN),
        PauseActionScript(NPC_0, identifier="EVENT_392_pause_action_script_2"),
        SetSyncActionScript(NPC_0, A0133_MK_OCCUPIED_EXTERIOR_REPEATING_HENCHMEN),
        Pause(240),
        PauseActionScript(NPC_1),
        SetSyncActionScript(NPC_1, A0133_MK_OCCUPIED_EXTERIOR_REPEATING_HENCHMEN),
        Pause(240),
        Jmp(["EVENT_392_pause_action_script_2"]),
    ]
)
