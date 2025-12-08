# pylint: disable=C0301

"""E2570_BOOSTER_PASS_SECRET_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_10,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkSouthPixels(4),
                ASFaceSouthwest(),
            ]),
        ActionQueueSync(
            target=NPC_11, subscript=[ASSetWalkingSpeed(FASTEST), ASWalkNorthPixels(8)]
        ),
        ActionQueueAsync(
            target=NPC_12, subscript=[ASSetWalkingSpeed(FASTEST), ASWalkWestPixels(8)]
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_10,
            R405_BOOSTER_PASS_SECRET,
            ["EVENT_2570_jmp_if_object_trigger_disabled_5"]),
        SetSyncActionScript(NPC_10, A0014_FLOATING_CHEST),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_11,
            R405_BOOSTER_PASS_SECRET,
            ["EVENT_2570_jmp_if_object_trigger_disabled_7"],
            identifier="EVENT_2570_jmp_if_object_trigger_disabled_5"),
        SetSyncActionScript(NPC_11, A0014_FLOATING_CHEST),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_12,
            R405_BOOSTER_PASS_SECRET,
            ["EVENT_2570_run_background_event_9"],
            identifier="EVENT_2570_jmp_if_object_trigger_disabled_7"),
        SetSyncActionScript(NPC_12, A0014_FLOATING_CHEST),
        RunBackgroundEvent(
            event_id=E2571_BOOSTER_PASS_SECRET_BACKGROUND,
            return_on_level_exit=True,
            identifier="EVENT_2570_run_background_event_9"),
        RunEventAsSubroutine(
            E0880_BOOSTER_PASS_SECRET_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
