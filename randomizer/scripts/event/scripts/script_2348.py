# E2348_TOWER_BULLET_BILL_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO000_SILENCE, channel=6),
        JmpIfObjectInCurrentLevel(
            NPC_4, ["EVENT_2348_jmp_if_present_in_current_level_3"]
        ),
        ActionQueueSync(
            target=NPC_4, subscript=[ASShiftNorthPixels(8), ASFaceSouthwest()]
        ),
        JmpIfObjectInCurrentLevel(
            NPC_5,
            ["EVENT_2348_jmp_if_present_in_current_level_5"],
            identifier="EVENT_2348_jmp_if_present_in_current_level_3",
        ),
        ActionQueueSync(
            target=NPC_5, subscript=[ASShiftWestPixels(18), ASFaceNortheast()]
        ),
        JmpIfObjectInCurrentLevel(
            NPC_6,
            ["EVENT_2348_jmp_if_present_in_current_level_7"],
            identifier="EVENT_2348_jmp_if_present_in_current_level_5",
        ),
        ActionQueueSync(
            target=NPC_6, subscript=[ASShiftNorthPixels(8), ASFaceSouthwest()]
        ),
        JmpIfObjectInCurrentLevel(
            NPC_8,
            ["EVENT_2348_action_queue_async_9"],
            identifier="EVENT_2348_jmp_if_present_in_current_level_7",
        ),
        ActionQueueSync(
            target=NPC_8, subscript=[ASShiftSoutheastPixels(8), ASFaceNortheast()]
        ),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftWestPixels(20),
                ASShiftSouthPixels(4),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASVisibilityOff(),
            ],
            identifier="EVENT_2348_action_queue_async_9",
        ),
        RunEventAsSubroutine(
            E0799_TOWER_JUMPING_SPOOKUM_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
