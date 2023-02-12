# E1312_TOWER_LOBBY_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PauseActionScript(NPC_4),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASSetWalkingSpeed(VERY_FAST), ASShiftSoutheastPixels(6)],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftSoutheastPixels(9),
                ASShiftSouthwestPixels(12),
                ASFaceSouthwest(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
                ASShiftNortheastPixels(4),
                ASShiftSoutheastPixels(5),
                ASSetPriority(1),
                ASShadowOff(),
            ],
        ),
        RunEventAsSubroutine(E0797_TOWER_LOBBY_SHUFFLED_NPC_ANIMATION_LOADER),
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM,
            ["EVENT_1312_pause_action_script_8"],
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_2,
            R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM,
            ["EVENT_1312_pause_action_script_8"],
        ),
        FadeInFromBlack(sync=False),
        Return(),
        PauseActionScript(NPC_1, identifier="EVENT_1312_pause_action_script_8"),
        PauseActionScript(NPC_2),
        RemoveObjectFromSpecificLevel(NPC_1, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM),
        RemoveObjectFromSpecificLevel(NPC_2, R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
